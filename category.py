from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class categoryClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("STOCKMATES - INVENTORY MANAGEMENT SYSTEM")
        self.root.config(bg="#87CEEB")  # Set background color to cream
        self.root.focus_force()
        
        # Variables
        self.var_cat_id = StringVar()
        self.var_name = StringVar()
        
        # Title
        lbl_title = Label(self.root, text="Manage Product Category", font=("goudy old style", 30), bg="#184a45", fg="white", bd=3, relief=RIDGE)
        lbl_title.pack(side=TOP, fill=X, padx=10, pady=20)
        
        lbl_cat_id = Label(self.root, text="Enter Category ID", font=("goudy old style", 30), bg="#FFFDD0")  # Change background color to cream
        lbl_cat_id.place(x=50, y=100)
        
        entry_cat_id = Entry(self.root, textvariable=self.var_cat_id, font=("goudy old style", 18), bg="lightyellow")
        entry_cat_id.place(x=50, y=170, width=300)
        
        lbl_name = Label(self.root, text="Enter Category Name", font=("goudy old style", 30), bg="#FFFDD0")  # Change background color to cream
        lbl_name.place(x=50, y=220)
        
        entry_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 18), bg="lightyellow")
        entry_name.place(x=50, y=290, width=300)
        
        btn_add = Button(self.root, text="ADD", font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2", command=self.add)
        btn_add.place(x=360, y=290, width=150, height=30)
        
        btn_delete = Button(self.root, text="DELETE", font=("goudy old style", 15), bg="red", fg="white", cursor="hand2", command=self.delete)
        btn_delete.place(x=520, y=290, width=150, height=30)
        
        # Image Display for the Table Area
        img_table_area = Image.open("images/cat.jpeg")  # Ensure the path is correct
        img_table_area = img_table_area.resize((900, 900), Image.LANCZOS)  # Resize image if needed
        self.img_table_area = ImageTk.PhotoImage(img_table_area)

        lbl_image_table_area = Label(self.root, image=self.img_table_area, bg="#FFFDD0")  # Set background color to cream
        lbl_image_table_area.place(x=700, y=100, width=831, height=500)  # Adjust size and position as needed
        
        # Category Details Table
        cat_frame = Frame(self.root, bd=3, relief=RIDGE, bg="#FFFDD0")  # Set background color to cream
        cat_frame.place(x=0, y=400, width=600, height=300)  # Adjusted width for the table frame

        scrolly = Scrollbar(cat_frame, orient=VERTICAL)
        scrollx = Scrollbar(cat_frame, orient=HORIZONTAL)

        self.categoryTable = ttk.Treeview(cat_frame, columns=("cid", "name"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)

        self.categoryTable.heading("cid", text="C ID")
        self.categoryTable.heading("name", text="Name")
        
        self.categoryTable["show"] = "headings"

        self.categoryTable.column("cid", width=100)  # Adjusted width for C ID column
        self.categoryTable.column("name", width=200)  # Adjusted width for Name column
        
        self.categoryTable.pack(fill=BOTH, expand=1)
        self.categoryTable.bind("<ButtonRelease-1>", self.get_data)

        # Load category data
        self.show()

    def get_data(self, event):
        selected_item = self.categoryTable.selection()
        if selected_item:
            item = self.categoryTable.item(selected_item)
            values = item['values']
            # Do something with the selected values
            print("Selected Item:", values)
            self.var_cat_id.set(values[0])
            self.var_name.set(values[1])

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "" or self.var_name.get() == "":
                messagebox.showerror("Error", "Category ID and Name are required", parent=self.root)
            else:
                cur.execute("INSERT INTO category (cat_id, name) VALUES (?, ?)", (self.var_cat_id.get(), self.var_name.get()))
                con.commit()
                messagebox.showinfo("Success", "Category Added Successfully", parent=self.root)
                self.show()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_cat_id.get() == "":
                messagebox.showerror("Error", "Select a Category to delete", parent=self.root)
            else:
                cur.execute("DELETE FROM category WHERE cat_id=?", (self.var_cat_id.get(),))
                con.commit()
                messagebox.showinfo("Success", "Category Deleted Successfully", parent=self.root)
                self.show()
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            rows = cur.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('', 'end', values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        finally:
            con.close()

    def clear(self):
        self.var_cat_id.set("")
        self.var_name.set("")

if __name__ == "__main__":
    root = Tk()
    obj = categoryClass(root)
    root.mainloop()
