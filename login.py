from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # Import from Pillow
import sqlite3
import os

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("1600x950+0+0")  # Use 'x' instead of '*'

        # ============images============
        # Open and resize the image (increase size to 500x500 for example)
        self.original_image = Image.open("done_img.jpg")
        self.resized_image = self.original_image.resize((500, 500), Image.LANCZOS)  # Resize to 500x500 or your preferred size
        self.phone_image = ImageTk.PhotoImage(self.resized_image)

        # Shift the image to the right (x=250) and down (y=120) and display it
        self.lbl_Phone_image = Label(self.root, image=self.phone_image)
        self.lbl_Phone_image.place(x=250, y=120)

        # =====Login_Frame========
        self.employee_id = StringVar()
        self.password = StringVar()
        # Creating the login frame
        login_frame = Frame(self.root, bd=5, relief=RIDGE)
        login_frame.place(x=800, y=150, width=350, height=400)  # Moved frame higher by reducing y to 150

        # Title inside the login frame
        lbl_title = Label(login_frame, text="Login Here", font=("Arial", 20, "bold"), fg="blue")
        lbl_title.place(x=90, y=30)

        # Employee ID label and text entry
        lbl_user = Label(login_frame, text="Employee ID", font=("Arial", 15, "bold"))
        lbl_user.place(x=30, y=100)

        self.txt_user = Entry(login_frame, textvariable=self.employee_id, font=("Arial", 15))
        self.txt_user.place(x=30, y=140, width=280)

        # Password label and text entry
        lbl_pass = Label(login_frame, text="Password", font=("Arial", 15, "bold"))
        lbl_pass.place(x=30, y=190)

        self.txt_pass = Entry(login_frame, show="*", textvariable=self.password, font=("Arial", 15))
        self.txt_pass.place(x=30, y=230, width=280)

        # Login button (linked to the login method)
        btn_login = Button(login_frame, command=self.login, text="Login", font=("Arial", 15, "bold"), bg="green", fg="white")
        btn_login.place(x=120, y=300)

    def login(self):
        print("Login button clicked")  # Added to track when the login function is triggered

        # Fetching employee_id and password
        eid = self.txt_user.get().strip()  # Use .strip() to remove leading/trailing spaces
        password = self.txt_pass.get().strip()

        # Debugging: Print employee_id and password
        print(f"Employee ID entered: '{eid}'")
        print(f"Password entered: '{password}'")

        # Check if fields are empty
        if eid == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            # Connect to the database
            conn = sqlite3.connect('ims.db')
            cursor = conn.cursor()
            print("Database connected")

            # Query the database for the employee's credentials and user type
            cursor.execute("SELECT eid, pass, utype FROM employee WHERE eid=? AND pass=?", (eid, password))
            result = cursor.fetchone()
            print(f"Query executed. Result: {result}")

            # Close the connection after fetching the result
            conn.close()

            # Check if the query result is None (incorrect credentials)
            if result is None:
                messagebox.showerror("Error", "Invalid Employee ID or Password")
            else:
                utype = result[2]  # Fetching the utype
                print(f"User Type: {utype}")
                messagebox.showinfo("Information", f"Welcome: {eid}")
                self.root.destroy()  # Close the login window

                # Open the appropriate application based on user type
                if utype == "Admin" or utype== "admin":  # Ensure correct comparison for admin
                    print("Redirecting to Admin dashboard")
                    if os.path.exists("dashboard.py"):
                        print("Opening dashboard.py for Admin")
                        os.system("python dashboard.py")  # Open the dashboard for Admin
                    else:
                        print("dashboard.py not found")
                        messagebox.showerror("Error", "Dashboard not found.")
                elif utype == "Employee" or utype=="employee":  # For Employee user type (capitalized)
                    print("Redirecting to Billing system")
                    if os.path.exists("billing.py"):
                        print("Opening billing.py for Employee")
                        os.system("python billing.py")  # Open the billing system for Employee
                    else:
                        print("billing.py not found")
                        messagebox.showerror("Error", "Billing system not found.")

        except sqlite3.Error as e:
            # Handle database connection errors
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            print(f"Database Error: {e}")

# Initialize the main window and the login system
root = Tk()
obj = Login_System(root)
root.mainloop()
