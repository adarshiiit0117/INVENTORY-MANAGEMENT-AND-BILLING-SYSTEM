from tkinter import *
from tkinter import ttk, messagebox
import sqlite3
from datetime import datetime

class ProductClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("STOCKMATES - INVENTORY MANAGEMENT SYSTEM")
        self.root.config(bg="#87CEEB")
        self.root.focus_force()

        # Product Frame
        self.product_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        self.product_frame.place(x=10, y=10, width=500, height=480)

        self.title_label = Label(self.product_frame, text="Product Details", bg="lightblue", fg="black",
                                 font=("Goudy Old Style", 20, "bold"), borderwidth=0)
        self.title_label.place(x=30, y=20, height=50, width=340)

        # Labels
        self.create_label(x=20, y=100, text="Category ID", bg="lightgrey", color="black")
        self.create_label(x=20, y=160, text="Supplier ID", bg="lightgrey", color="black")
        self.create_label(x=20, y=220, text="Name", bg="lightgrey", color="black")
        self.create_label(x=20, y=280, text="Price", bg="lightgrey", color="black")
        self.create_label(x=20, y=340, text="Quantity", bg="lightgrey", color="black")
        self.create_label(x=20, y=400, text="Status", bg="lightgrey", color="black")

        # Input Fields
        self.category_entry = Entry(self.product_frame, font=("Goudy Old Style", 15))
        self.category_entry.place(x=155, y=100, width=230)

        self.supplier_entry = Entry(self.product_frame, font=("Goudy Old Style", 15))  # Replaced Combobox with Entry
        self.supplier_entry.place(x=155, y=160, width=230)

        self.name_entry = Entry(self.product_frame, font=("Goudy Old Style", 15))
        self.name_entry.place(x=155, y=220, width=230)

        self.price_entry = Entry(self.product_frame, font=("Goudy Old Style", 15))
        self.price_entry.place(x=155, y=280, width=230)

        self.quantity_entry = Entry(self.product_frame, font=("Goudy Old Style", 15))
        self.quantity_entry.place(x=155, y=340, width=230)

        self.status_combobox = ttk.Combobox(self.product_frame, values=["Available", "Out of Stock"],
                                            font=("Goudy Old Style", 15))
        self.status_combobox.place(x=155, y=400, width=230)
        self.status_combobox.current(0)

        # Buttons
        btn_add = Button(self.product_frame, text="Save", command=self.add, font=("Goudy Old Style", 15), bg="#2196f3", fg="white", cursor="hand2")
        btn_add.place(x=20, y=440, width=110, height=28)

        btn_update = Button(self.product_frame, text="Update", command=self.update, font=("Goudy Old Style", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_update.place(x=140, y=440, width=110, height=28)

        btn_delete = Button(self.product_frame, text="Delete", command=self.delete, font=("Goudy Old Style", 15), bg="#f44336", fg="white", cursor="hand2")
        btn_delete.place(x=260, y=440, width=110, height=28)

        btn_clear = Button(self.product_frame, text="Clear", command=self.clear, font=("Goudy Old Style", 15), bg="#607d8b", fg="white", cursor="hand2")
        btn_clear.place(x=380, y=440, width=110, height=28)

        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Product", font=("Goudy Old Style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=530, y=10, width=800, height=70)

        self.var_searchby = StringVar()
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Category", "Supplier", "Name"), state='readonly', justify=CENTER, font=("Goudy Old Style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        self.var_searchtext = StringVar()
        txt_search = Entry(SearchFrame, textvariable=self.var_searchtext, font=("Goudy Old Style", 15), bg="lightyellow")
        txt_search.place(x=200, y=10, width=200)

        btn_search = Button(SearchFrame, text="Search", command=self.search, font=("Goudy Old Style", 15), bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=410, y=10, width=150, height=30)

        # Product Treeview
        self.result_tree = ttk.Treeview(self.root, columns=("id", "name", "category_id", "supplier_id", "price", "quantity", "status","date_added"), show='headings')
        self.result_tree.place(x=530, y=90, width=800, height=400)

        self.result_tree.heading("id", text="ID")
        self.result_tree.heading("name", text="Name")
        self.result_tree.heading("category_id", text="Category ID")
        self.result_tree.heading("supplier_id", text="Supplier ID")
        self.result_tree.heading("price", text="Price")
        self.result_tree.heading("quantity", text="Quantity")
        self.result_tree.heading("status", text="Status")
        self.result_tree.heading("date_added", text="Date Added")
        
        self.result_tree.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    def create_label(self, x, y, text, bg, color):
        label = Label(self.product_frame, text=text, bg=bg, fg=color, font=("Goudy Old Style", 15))
        label.place(x=x, y=y, height=30, width=130)

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            category_id = self.category_entry.get()
            supplier_id = self.supplier_entry.get()
            name = self.name_entry.get()
            price = self.price_entry.get()
            quantity = self.quantity_entry.get()
            status = self.status_combobox.get()

            if not name or not price or not quantity or not category_id or not supplier_id:
                messagebox.showerror("Error", "Please fill all fields", parent=self.root)
                return

            current_date = datetime.now().date() 
            cur.execute("""
            INSERT INTO product (category, supplier, name, price, quantity, status, date_added) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (category_id, supplier_id, name, price, quantity, status, current_date))  # Now passing current_date


            con.commit()
            messagebox.showinfo("Success", "Product Added Successfully", parent=self.root)
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            category_id = self.category_entry.get()
            supplier_id = self.supplier_entry.get()
            name = self.name_entry.get()
            price = self.price_entry.get()
            quantity = self.quantity_entry.get()
            status = self.status_combobox.get()

            if not name or not price or not quantity or not category_id or not supplier_id:
                messagebox.showerror("Error", "Please fill all fields", parent=self.root)
                return
            current_date = datetime.now().date()
            cur.execute("UPDATE product SET category=?, supplier=?, price=?, quantity=?, status=? ,date_added=? WHERE name=?",
                        (category_id, supplier_id, price, quantity, status, current_date, name))
            con.commit()
            messagebox.showinfo("Success", "Product Updated Successfully", parent=self.root)
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()
    

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            name = self.name_entry.get()
            if not name:
                messagebox.showerror("Error", "Please select a product to delete", parent=self.root)
                return
            cur.execute("DELETE FROM product WHERE name=?", (name,))
            con.commit()
            messagebox.showinfo("Success", "Product Deleted Successfully", parent=self.root)
            self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.name_entry.delete(0, END)
        self.category_entry.delete(0, END)
        self.supplier_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.quantity_entry.delete(0, END)
        self.status_combobox.current(0)
        self.show()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            rows = cur.fetchall()
            self.result_tree.delete(*self.result_tree.get_children())
            for row in rows:
                self.result_tree.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def get_data(self, ev):
        f = self.result_tree.focus()
        content = self.result_tree.item(f)
        row = content['values']
        self.name_entry.delete(0, END)
        self.category_entry.delete(0, END)
        self.supplier_entry.delete(0, END)
        self.price_entry.delete(0, END)
        self.quantity_entry.delete(0, END)

        self.category_entry.insert(END, row[2])
        self.supplier_entry.insert(END, row[3])
        self.name_entry.insert(END, row[1])
        self.price_entry.insert(END, row[4])
        self.quantity_entry.insert(END, row[5])
        self.status_combobox.set(row[6])

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            search_by = self.var_searchby.get()
            search_text = self.var_searchtext.get()
            if search_by == "Select":
                messagebox.showerror("Error", "Please select search criteria", parent=self.root)
            elif search_by == "Category":
                cur.execute("SELECT * FROM product WHERE category LIKE ?", ('%' + search_text + '%',))
            elif search_by == "Supplier":
                cur.execute("SELECT * FROM product WHERE supplier LIKE ?", ('%' + search_text + '%',))
            elif search_by == "Name":
                cur.execute("SELECT * FROM product WHERE name LIKE ?", ('%' + search_text + '%',))
            rows = cur.fetchall()
            if len(rows) == 0:
                messagebox.showinfo("No Results", "No matching records found", parent=self.root)
            self.result_tree.delete(*self.result_tree.get_children())
            for row in rows:
                self.result_tree.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = ProductClass(root)
    root.mainloop()
