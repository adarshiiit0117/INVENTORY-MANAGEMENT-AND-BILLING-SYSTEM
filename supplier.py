from tkinter import *
from tkinter import ttk, messagebox
import sqlite3

class SupplierClass:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("STOCKMATES - INVENTORY MANAGEMENT SYSTEM")
        self.root.config(bg="#87CEEB")
        self.root.focus_force()

        # Variables
        self.var_searchby = StringVar()
        self.var_searchtext = StringVar()
        self.var_sup_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()

        # Search Frame
        SearchFrame = LabelFrame(self.root, text="Search Supplier", font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE, bg="white")
        SearchFrame.place(x=250, y=20, width=600, height=70)

        # Search Options
        cmb_search = ttk.Combobox(SearchFrame, textvariable=self.var_searchby, values=("Select", "Invoice No.", "Name", "Contact"), state='readonly', justify=CENTER, font=("goudy old style", 15))
        cmb_search.place(x=10, y=10, width=180)
        cmb_search.current(0)

        txt_search = Entry(SearchFrame, textvariable=self.var_searchtext, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=10)
        btn_search = Button(SearchFrame, text="Search", command=self.search, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=410, y=9, width=150, height=30)

        # Title
        title = Label(self.root, text="Supplier Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white").place(x=50, y=100, width=1000)

        # Content - Supplier Details Form
        # Row 1
        lbl_supplier_invoice = Label(self.root, text="Invoice No.", font=("goudy old style", 15), bg="white").place(x=50, y=150)
        txt_supplier_invoice = Entry(self.root, textvariable=self.var_sup_invoice, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=150, width=180)

        # Row 2
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=190)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=190, width=180)

        # Row 3
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=50, y=230)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15), bg="lightyellow").place(x=200, y=230, width=180)

        # Row 4
        lbl_desc = Label(self.root, text="Description", font=("goudy old style", 15), bg="white").place(x=50, y=270)
        self.txt_desc = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_desc.place(x=200, y=270, width=300, height=60)

        # Buttons
        btn_add = Button(self.root, text="Save", command=self.add, font=("goudy old style", 15), bg="#2196f3", fg="white", cursor="hand2").place(x=200, y=340, width=110, height=35)
        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style", 15), bg="#4caf50", fg="white", cursor="hand2").place(x=320, y=340, width=110, height=35)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15), bg="#f44336", fg="white", cursor="hand2").place(x=440, y=340, width=110, height=35)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15), bg="#607d8b", fg="white", cursor="hand2").place(x=560, y=340, width=110, height=35)

        # Supplier Details Table
        supplier_frame = Frame(self.root, bd=3, relief=RIDGE)
        supplier_frame.place(x=0, y=400, relwidth=1, height=300)

        scrolly = Scrollbar(supplier_frame, orient=VERTICAL)
        scrollx = Scrollbar(supplier_frame, orient=HORIZONTAL)

        self.supplierTable = ttk.Treeview(supplier_frame, columns=("invoice", "name", "contact", "desc"), yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("invoice", text="Invoice No.")
        self.supplierTable.heading("name", text="Name")
        self.supplierTable.heading("contact", text="Contact")
        self.supplierTable.heading("desc", text="Description")
        
        self.supplierTable["show"] = "headings"

        self.supplierTable.column("invoice", width=90)
        self.supplierTable.column("name", width=100)
        self.supplierTable.column("contact", width=100)
        self.supplierTable.column("desc", width=150)
        
        self.supplierTable.pack(fill=BOTH, expand=1)
        self.supplierTable.bind("<ButtonRelease-1>", self.get_data)

        self.show()

    # Function to add a supplier to the database
    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice = ?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This Invoice No. already exists", parent=self.root)
                else:
                    cur.execute("INSERT INTO supplier (invoice, name, contact, desc) VALUES (?, ?, ?, ?)", (
                        self.var_sup_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0', END).strip(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Added Successfully", parent=self.root)
                    self.show()
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    # Function to fetch supplier data from the database
    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supplier")
            rows = cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in rows:
                self.supplierTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    # Function to get selected row data
    def get_data(self, ev):
        f = self.supplierTable.focus()
        content = self.supplierTable.item(f)
        row = content['values']
        
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0', END)
        self.txt_desc.insert(END, row[3])

    # Function to update a supplier's information
    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice = ?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("UPDATE supplier SET name=?, contact=?, desc=? WHERE invoice=?", (
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.txt_desc.get('1.0', END).strip(),
                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Updated Successfully", parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    # Function to delete a supplier's information
    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_sup_invoice.get() == "":
                messagebox.showerror("Error", "Invoice No. must be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM supplier WHERE invoice = ?", (self.var_sup_invoice.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Invoice No.", parent=self.root)
                else:
                    cur.execute("DELETE FROM supplier WHERE invoice=?", (self.var_sup_invoice.get(),))
                    con.commit()
                    messagebox.showinfo("Success", "Supplier Deleted Successfully", parent=self.root)
                    self.show()
                    self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    # Function to clear input fields
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0', END)

    # # Function to search suppliers based on the given criteria
    # def search(self):
    #     con = sqlite3.connect(database=r'ims.db')
    #     cur = con.cursor()
    #     try:
    #     # Validate search criteria selection
    #         if self.var_searchby.get() == "Select":
    #              messagebox.showerror("Error", "Select a search criteria", parent=self.root)
    #     # Validate search text input
    #         elif self.var_searchtext.get() == "":
    #             messagebox.showerror("Error", "Search text must be required", parent=self.root)
    #         else:
    #         # Dynamically construct the query without passing the column name as a parameter
    #             search_column = self.var_searchby.get().replace(' ', '_').lower()
    #             query = f"SELECT * FROM supplier WHERE {search_column} LIKE ?"
    #             cur.execute(query, ('%' + self.var_searchtext.get() + '%',))

    #         # Fetch all matching rows
    #             rows = cur.fetchall()

    #         # Clear existing data from the table
    #             self.supplierTable.delete(*self.supplierTable.get_children())

    #         # Insert fetched rows into the table
    #             for row in rows:
    #                 self.supplierTable.insert('', END, values=row)

    #     except Exception as ex:
    #     # Display error message if any exception occurs
    #         messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    #     finally:
    #     # Ensure the database connection is closed
    #         con.close()
    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
        # Validate search criteria selection
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Select a search criteria", parent=self.root)
        
        # Validate search text input
            elif self.var_searchtext.get() == "":
                messagebox.showerror("Error", "Search text must be required", parent=self.root)
        
            else:
            # Define a mapping between search options and actual database columns
                search_column_map = {
                "Invoice No.": "invoice",
                "Name": "name",
                "Contact": "contact"
            }
            
            # Get the correct column name from the map
                search_column = search_column_map.get(self.var_searchby.get())
            
            # Check if the column is valid
                if not search_column:
                    messagebox.showerror("Error", "Invalid search criteria", parent=self.root)
                    return
            
            # Execute the search query
                query = f"SELECT * FROM supplier WHERE {search_column} LIKE ?"
                search_text = '%' + self.var_searchtext.get() + '%'
            
            # Debugging: Print the query and search text
                print(f"Executing Query: {query}")
                print(f"Search Text: {search_text}")

                cur.execute(query, (search_text,))
                rows = cur.fetchall()

            # Debugging: Print number of fetched rows
                print(f"Number of rows found: {len(rows)}")

            # Clear existing data from the table
                self.supplierTable.delete(*self.supplierTable.get_children())

            # If no rows are found, show a message
                if len(rows) == 0:
                    messagebox.showinfo("Info", "No matching records found", parent=self.root)
                else:
                # Insert fetched rows into the table
                    for row in rows:
                        self.supplierTable.insert('', END, values=row)

        except Exception as ex:
        # Display error message if any exception occurs
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
        # Debugging: Print the exception for further investigation
            print(f"Exception occurred: {ex}")
    
        finally:
        # Ensure the database connection is closed
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = SupplierClass(root)
    root.mainloop()
