# Inventory Management System (IMS) and Billing system

## Project Overview

**Name:** Inventory Management System (IMS)  
**Type:** Desktop Application  
**Technology Stack:**  
- **UI:** Tkinter (Python GUI Library)  
- **Database:** SQLite (Relational Database)  
- **Language:** Python  

**Purpose:**  
The IMS is designed to manage inventory records, including products, suppliers, and stock. The system allows users to add, update, delete, and view products, suppliers, and other details through an intuitive user interface.

---

## Core Features

### 1. Login System
- **Role-based Access Control:**
  - Admins and employees can log in using unique credentials.
  - Access levels vary based on user roles.

### 2. Product Management
- Add new product details such as name, category, quantity, and price.
- Update existing product records.
- Delete products from the system.
- View the list of all products in the inventory.

### 3. Supplier Management
- Add, update, and delete supplier details, including name, contact information, and supplied items.
- View the list of all registered suppliers.

### 4. User Interface
- **Tkinter-based GUI:**
  - Responsive and user-friendly design.
  - Separate frames/windows for each functionality (e.g., product management, supplier management).

---

## User Roles

### 1. Admin
- **Permissions:**
  - Full access to all features, including product management, supplier management, and employee management.

### 2. Employee
- **Permissions:**
  - Limited to the Billing Module.
  - Can create and manage sales transactions.
  - Cannot modify product or supplier details.

---

## Installation and Setup

### Prerequisites
- Python 3.x installed on your system.
- SQLite (included by default with Python).

### Steps to Run
1. Clone or download the project repository.
2. Navigate to the project directory.
3. Install required dependencies (if any):
   ```bash
   pip install -r requirements.txt
   ```
4. Run the main Python script to start the application:
   ```bash
   python main.py
   ```

---

## Project Structure

- **main.py:** Entry point of the application.
- **ui/**: Contains GUI design files and Tkinter scripts.
- **database/**: Includes SQLite database and scripts for database setup.
- **modules/**: Core logic for product and supplier management.

---

## Future Enhancements

- Add reporting features (e.g., sales reports, inventory reports).
- Implement a search functionality for products and suppliers.
- Introduce barcode scanning for product entries.
- Integrate email notifications for low stock alerts.

---
![image](https://github.com/user-attachments/assets/fe610561-4ecf-4d27-b1d4-77f371ffd85c)


![image](https://github.com/user-attachments/assets/1b171270-c64c-43d4-8c78-48e38ba89497)
![image](https://github.com/user-attachments/assets/c282c1a3-ba79-4cd8-83ff-34759a0a2e9c)
![image](https://github.com/user-attachments/assets/61840884-4d4a-4ad7-b405-d3e381aa52b1)
![image](https://github.com/user-attachments/assets/1c391725-0b6c-4ef2-b2df-1c1e80929f0c)
![image](https://github.com/user-attachments/assets/8700d3c0-6a79-4549-ab6a-3d22d07c2e96)
![image](https://github.com/user-attachments/assets/785a1a7e-b984-4cc7-a26a-d8078688b69a)





