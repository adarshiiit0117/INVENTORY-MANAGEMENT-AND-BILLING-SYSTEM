import sqlite3

def create_db():
    try:
        # Connect to the SQLite database (or create it if it doesn't exist)
        con = sqlite3.connect('ims.db')
        cur = con.cursor()

        # Create 'employee' table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                eid INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                email TEXT,
                gender TEXT,
                contact TEXT,
                dob TEXT,
                doj TEXT,
                pass TEXT,
                utype TEXT,
                address TEXT,
                salary TEXT
            )
        """)

        # Create 'supplier' table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS supplier (
                invoice INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                contact TEXT,
                desc TEXT
            )
        """)

        # Create 'category' table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS category (
                cat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT
            )
        """)

        # Create 'product' table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                category TEXT,
                supplier TEXT,
                price REAL,
                quantity INTEGER,
                status TEXT,
                date_added TEXT
            )
        """)

        # Create 'sales' table
        cur.execute('''CREATE TABLE IF NOT EXISTS sales (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        invoice_no TEXT,
                        customer_name TEXT,
                        sale_date TEXT,
                        amount REAL)''')

        # Commit the changes and close the connection
        con.commit()
        con.close()
        print("Tables created successfully")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

# Call the function to create the database and all tables
create_db()
