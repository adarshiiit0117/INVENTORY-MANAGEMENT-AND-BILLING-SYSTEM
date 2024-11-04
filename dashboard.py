from tkinter import *
from PIL import Image, ImageTk
from employee import employeeClass
from supplier import SupplierClass
from category import categoryClass
from product import ProductClass  # Import the ProductClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("STOCKMATES - INVENTORY MANAGEMENT SYSTEM")
        self.root.config(bg="#87CEEB")

        # Load the icon image for the title
        self.icon_title = Image.open("images/logo.png")
        self.icon_title = self.icon_title.resize((50, 50), Image.Resampling.LANCZOS)
        self.icon_title = ImageTk.PhotoImage(self.icon_title)

        # ----title----
        title = Label(self.root, text="INVENTORY MANAGEMENT SYSTEM", image=self.icon_title, compound=LEFT,
                      font=("times new roman", 40, "bold"), bg="#010c40", fg="white", anchor="w", padx=20)
        title.place(x=0, y=0, relwidth=1, height=70)

        # Logout button
        btn_logout = Button(self.root, text="Logout", command=self.logout, font=("times new roman", 15, "bold"),
                            bg="yellow", cursor="hand2")
        btn_logout.place(x=1150, y=10, height=50, width=150)

        # Clock
        self.lbl_clock = Label(self.root, text="WELCOME TO STOCKMATES\t\t Date:DD-MM-YYYY\t\t Time:HH:MM:SS",
                               font=("times new roman", 15), bg="#4d636d", fg="white")
        self.lbl_clock.place(x=0, y=70, relwidth=1, height=30)
        self.update_clock()  # Initialize clock update

        # Left menu
        self.MenuLogo = Image.open("images/logo1.png")
        self.MenuLogo = self.MenuLogo.resize((200, 200), Image.Resampling.LANCZOS)
        self.MenuLogo = ImageTk.PhotoImage(self.MenuLogo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=5, y=100, width=200, height=599)  # Adjusted height
        lbl_MenuLogo = Label(LeftMenu, image=self.MenuLogo)
        lbl_MenuLogo.pack(side=TOP, fill=X)

        # MENU Label
        lbl_menu = Label(LeftMenu, text="MENU", font=("times new roman", 20), bg="#009688")
        lbl_menu.pack(side=TOP, fill=X)

        # Load and resize side.png image
        self.side_image = Image.open("images/side.png")
        self.side_image = self.side_image.resize((30, 30), Image.Resampling.LANCZOS)
        self.side_image = ImageTk.PhotoImage(self.side_image)

        button_style = {
            'image': self.side_image,
            'compound': LEFT,
            'font': ("times new roman", 16, "bold"),
            'bg': "white",
            'bd': 3,
            'cursor': "hand2",
            'padx': 5,
            'anchor': "w"
        }

        # Employee Button
        btn_employee = Button(LeftMenu, text="EMPLOYEE", command=self.employee, **button_style)
        btn_employee.pack(side=TOP, fill=X)

        # Supplier Button
        btn_supplier = Button(LeftMenu, text="SUPPLIER", command=self.supplier, **button_style)
        btn_supplier.pack(side=TOP, fill=X)

        # Category Button
        btn_category = Button(LeftMenu, text="CATEGORY", command=self.category, **button_style)
        btn_category.pack(side=TOP, fill=X)

        # Products Button
        btn_products = Button(LeftMenu, text="PRODUCTS", command=self.products, **button_style)
        btn_products.pack(side=TOP, fill=X)

        # Sales Button
        btn_sales = Button(LeftMenu, text="SALES", command=self.sales, **button_style)
        btn_sales.pack(side=TOP, fill=X)

        # Exit Button
        btn_exit = Button(LeftMenu, text="EXIT", command=self.exit_app, **button_style)
        btn_exit.pack(side=TOP, fill=X)

        # Content Labels
        #self.total_employee = self.create_label(x=300, y=120, text="Total Employee\n[ 0 ]", bg="#33bbf9", color="white")
        #self.total_supplier = self.create_label(x=650, y=120, text="Total Supplier\n[ 0 ]", bg="#ff5733", color="white")
        #self.total_category = self.create_label(x=1000, y=120, text="Total Category\n[ 0 ]", bg="#33ff57", color="black")
        #self.total_products = self.create_label(x=300, y=300, text="Total Products\n[ 0 ]", bg="#ff33a8", color="white")
        #self.total_sales = self.create_label(x=650, y=300, text="Total Sales\n[ 0 ]", bg="#33aaff", color="black")

        # Footer
        footer = Label(self.root, text="Inventory Management System developed by StockMates",
                       font=("times new roman", 12), bg="black", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        # Fetch and update counts
        self.update_counts()

    def create_label(self, x, y, text, bg, color):
        """Helper function to create labels with specified properties."""
        label = Label(self.root, text=text, bg=bg, fg=color, font=("Goudy Old Style", 20, "bold"),
                      borderwidth=2, relief="solid")
        label.place(x=x, y=y, height=150, width=300)
        return label

    def update_counts(self):
        """Fetch counts from the database and update the labels."""
        # Example: Replace the following with actual database queries
        # For demonstration, using static values
        total_employee = self.get_total_employee()
        total_supplier = self.get_total_supplier()
        total_category = self.get_total_category()
        total_products = self.get_total_products()
        total_sales = self.get_total_sales()

        #self.total_employee.config(text=f"Total Employee\n[ {total_employee} ]")
        #self.total_supplier.config(text=f"Total Supplier\n[ {total_supplier} ]")
        #self.total_category.config(text=f"Total Category\n[ {total_category} ]")
        #self.total_products.config(text=f"Total Products\n[ {total_products} ]")
        #self.total_sales.config(text=f"Total Sales\n[ {total_sales} ]")

    def get_total_employee(self):
        # Implement actual database query to get total employees
        return 10  # Placeholder

    def get_total_supplier(self):
        # Implement actual database query to get total suppliers
        return 5  # Placeholder

    def get_total_category(self):
        # Implement actual database query to get total categories
        return 8  # Placeholder

    def get_total_products(self):
        # Implement actual database query to get total products
        return 50  # Placeholder

    def get_total_sales(self):
        # Implement actual database query to get total sales
        return 20  # Placeholder

    def update_clock(self):
        """Update the clock every second."""
        from time import strftime
        current_time = strftime("%d-%m-%Y %H:%M:%S")
        self.lbl_clock.config(text=f"WELCOME TO STOCKMATES\t\t Date:{current_time.split()[0]}\t\t Time:{current_time.split()[1]}")
        self.lbl_clock.after(1000, self.update_clock)

    def employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = employeeClass(self.new_win)

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = SupplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)

    def products(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ProductClass(self.new_win)  # Open the Products window

    def sales(self):
        self.new_win = Toplevel(self.root)
        # Assuming you have a SalesClass defined similarly
      
        self.new_obj = salesClass(self.new_win)

    def logout(self):
        # Implement logout functionality
        from tkinter import messagebox
        confirm = messagebox.askyesno("Logout", "Do you really want to logout?")
        if confirm:
            self.root.destroy()
            # Optionally, redirect to login window

    def exit_app(self):
        # Implement exit functionality
        from tkinter import messagebox
        confirm = messagebox.askyesno("Exit", "Do you really want to exit?")
        if confirm:
            self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)
    root.mainloop()
