import os
from tkinter import *
from tkinter import messagebox

class salesClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System | Developed By Rangesh")
        self.root.geometry("1000x600+300+100")
        self.root.config(bg="white")

        # Title
        title = Label(self.root, text="View Customer Bills", font=("times new roman", 30, "bold"), bg="#010c40", fg="white")
        title.pack(side=TOP, fill=X)

        # Invoice Number Search
        lbl_invoice = Label(self.root, text="Bill No.", font=("times new roman", 15, "bold"), bg="white")
        lbl_invoice.place(x=50, y=100)

        self.txt_invoice = Entry(self.root, font=("times new roman", 15), bg="lightyellow")
        self.txt_invoice.place(x=180, y=100, width=180)

        btn_search = Button(self.root, text="Search", command=self.search_bill, font=("times new roman", 15, "bold"),
                            bg="#4caf50", fg="white", cursor="hand2")
        btn_search.place(x=380, y=100, width=100, height=28)

        btn_clear = Button(self.root, text="Clear", command=self.clear_search, font=("times new roman", 15, "bold"),
                           bg="#f44336", fg="white", cursor="hand2")
        btn_clear.place(x=500, y=100, width=100, height=28)

        # Listbox for Invoice Files (on the left)
        self.bill_listbox = Listbox(self.root, font=("times new roman", 15), bg="lightgray")
        self.bill_listbox.place(x=50, y=150, width=200, height=400)
        self.bill_listbox.bind("<Double-Button-1>", self.show_bill)

        # Bill Display Area (center-right)
        lbl_bill_area = Label(self.root, text="Customer Bill Area", font=("times new roman", 18, "bold"), bg="orange", fg="black")
        lbl_bill_area.place(x=280, y=150, width=680, height=30)

        self.bill_text_area = Text(self.root, font=("times new roman", 15), bg="lightyellow")
        self.bill_text_area.place(x=280, y=180, width=680, height=370)

        self.load_bill_files()  # Load bill files on startup

    def load_bill_files(self):
        """
        This function loads all the .txt files from the 'bill/' folder and displays them in the Listbox.
        """
        bill_path = "bill/"  # Path to your folder containing bill files
        self.bill_listbox.delete(0, END)  # Clear the Listbox first

        try:
            files = [f for f in os.listdir(bill_path) if f.endswith(".txt")]  # Get only .txt files
            if files:
                for bill_file in files:
                    self.bill_listbox.insert(END, bill_file)  # Insert file names into the Listbox
            else:
                messagebox.showinfo("Info", "No bill files found")
        except Exception as e:
            messagebox.showerror("Error", f"Error accessing files: {str(e)}")

    def show_bill(self, event):
        """
        This function displays the content of the selected file in the Customer Bill Area.
        """
        selected_file = self.bill_listbox.get(self.bill_listbox.curselection())
        self.bill_text_area.delete(1.0, END)  # Clear the text area before showing new content

        bill_path = "bill/"  # Path to your folder containing bill files
        try:
            with open(bill_path + selected_file, 'r') as file:
                bill_content = file.read()
                self.bill_text_area.insert(END, bill_content)
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file: {str(e)}")

    def search_bill(self):
        invoice_no = self.txt_invoice.get()
        if invoice_no == "":
            messagebox.showerror("Error", "Invoice number is required")
        else:
            bill_path = "bill/"  # Path to your folder containing bill files
            self.bill_listbox.delete(0, END)  # Clear the listbox before inserting

            try:
                files = [f for f in os.listdir(bill_path) if invoice_no in f and f.endswith(".txt")]  # Search files containing the invoice number
                if files:
                    for bill_file in files:
                        self.bill_listbox.insert(END, bill_file)  # Insert matching files into the Listbox
                else:
                    messagebox.showinfo("Info", "No bill found for this invoice number")
            except Exception as e:
                messagebox.showerror("Error", f"Error accessing files: {str(e)}")

    def clear_search(self):
        self.txt_invoice.delete(0, END)
        self.bill_text_area.delete(1.0, END)
        self.bill_listbox.delete(0, END)
        self.load_bill_files()  # Reload all files after clearing search

if __name__ == "__main__":
    root = Tk()
    obj = BillViewClass(root)
    root.mainloop()
