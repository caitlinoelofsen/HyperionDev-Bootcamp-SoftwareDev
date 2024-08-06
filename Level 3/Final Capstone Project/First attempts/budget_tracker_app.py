import sqlite3
import os
import sys

class Budget_Tracker:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = self.connect_db()
        self.create_users_table()
        self.create_categories_table()
        self.create_budget_table()
        self.create_expenses_table()
        self.create_income_table()
        self.create_income_categories_table()
        self.current_user_id = None

    def connect_db(self):
        if not os.path.exists('data'):
            os.makedirs('data')
        return sqlite3.connect(self.db_path)

    def create_users_table(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(
                       user_id INTEGER PRIMARY KEY,
                       username TEXT,
                       email TEXT,
                       password TEXT
            )
        ''')
        self.db.commit()

    def create_categories_table(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories(
                       category_id INTEGER PRIMARY KEY,
                       category_name TEXT
            )
        ''')
        self.db.commit()

    def create_budget_table(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS budgets(
                       budget_id INTEGER PRIMARY KEY,
                       user_id INTEGER,
                       category_id INTEGER,
                       budget_amount REAL NOT NULL,
                       start_date DATE NOT NULL,
                       end_date DATE NOT NULL,
                       FOREIGN KEY(user_id) REFERENCES users(user_id),
                       FOREIGN KEY(category_id) REFERENCES categories(category_id)
            )
        ''')
        self.db.commit()

    def create_expenses_table(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS expenses(
                       expense_id INTEGER PRIMARY KEY,
                       user_id INTEGER,
                       category_id INTEGER,
                       amount REAL NOT NULL,
                       date DATE NOT NULL,
                       description TEXT,
                       FOREIGN KEY(user_id) REFERENCES users(user_id),
                       FOREIGN KEY(category_id) REFERENCES categories(category_id)
            )
        ''')
        self.db.commit()
    
    def create_income_table(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS incomes(
                       income_id INTEGER PRIMARY KEY,
                       user_id INTEGER,
                       category_id INTEGER,
                       amount REAL NOT NULL,
                       date DATE NOT NULL,
                       description TEXT,
                       FOREIGN KEY(user_id) REFERENCES users(user_id),
                       FOREIGN KEY(category_id) REFERENCES categories(category_id)
            )
        ''')
        self.db.commit()
    
    def create_income_categories_table(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS income_categories(
                       category_id INTEGER PRIMARY KEY,
                       category_name TEXT
            )
        ''')
        self.db.commit()

    @staticmethod
    def get_valid_input (prompt):
        while True:
            try:
                value = float(input(prompt))
                if value.is_integer():
                    return int(value)
                else:
                    return value
            except ValueError:
                print("invalid input. Please enter a valid number.")

    def register_user(self):
        username = input("Enter username: ")
        email = input("Enter email address: ")
        password = input("Enter password: ")
        cursor = self.db.cursor()
        try:
            cursor.execute("INSERT INTO OR IGNORE users (username, email, password) VALUES (?, ?, ?)",
                       (username, email, password))
            self.db.commit()
            print("User registered successfully.")
        except sqlite3.IntegrityError:
            print("Registration failed. Email may already be in use.")

    def login_user(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        cursor = self.db.cursor()
        cursor.execute("SELECT user_id FROM users WHERE email = ? AND password = ?",
                       (email, password))
        user = cursor.fetchone()
        if user:
            self.current_user_id = user[0]
            print("Login successful.")
        else:
            print("Invalid email or password.")

    def exit_program(self):
        print("Exiting the program...")
        self.db.close()
        sys.exit(0)

    def expense_menu(self):
        while True:
            option = input('''Enter a menu option:
                1. Add New Expense
                2. Update Expense Amount
                3. Add Expense Category
                4. Delete Expense Category
                5. View Expenses
                6. View Expense Categories
                7. Main Menu
            ''')
            if option == '1':
                self.add_new_expense()
            elif option == '2':
                self.update_expense_amount()
            elif option == '3':
                self.add_expense_category()
            elif option == '4':
                self.delete_expense_category()
            elif option == '5':
                self.view_expenses()
            elif option == '6':
                self.view_expense_categories()
            elif option == '7':
                break
            else:
                print("Invalid option. Please try again.") 

    def add_new_expense(self):
        category_id = self.get_valid_input("Enter category ID: ")
        amount = self.get_valid_input("Enter amount: ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")

        cursor = self.db.cursor()
        cursor.execute("SELECT category_id FROM categories WHERE category_id = ?",
                       (category_id,))
        if cursor.fetchone() is None:
            print(f"Category ID {category_id} does not exist. Please enter a valid ID.")
            return
        
        cursor.execute("INSERT OR IGNORE INTO expenses (user_id, category_id, amount, date, description) VALUES (?, ?, ?, ?, ?)",
                       (self.current_user_id, category_id, amount, date, description))
        self.db.commit()
        if cursor.rowcount == 0:
            print("Expense already exists.")
        else:
            print("Expense added successfully.")

    def update_expense_amount(self):
        expense_id = self.get_valid_input("Enter expense ID: ")
        new_amount = self.get_valid_input("Enter new amount: ")
        cursor = self.db.cursor()
        try:
            cursor.execute("UPDATE expenses SET amount = ? WHERE expense_id = ? AND user_id = ?", 
                       (new_amount, expense_id, self.current_user_id))
            self.db.commit()
            if cursor.rowcount == 0:
                print("No expense found with the given ID.")
            else:
                print("Expense amount updated successfully.")
        except sqlite3.IntegrityError:
            print("Failed to update the expense amount.")

    def add_expense_category(self):
        category_name = input("Enter new expense category name: ")
        cursor = self.db.cursor()
        try:
            cursor.execute("INSERT OR IGNORE INTO categories (category_name) VALUES (?)",
                       (category_name,))
            self.db.commit()
            if cursor.rowcount == 0:
                print("Expense category already exists.")
            else:
                print("Expense category added successfully.")
        except sqlite3.IntegrityError:
            print("Failed to add the expense category.")

    def delete_expense_category(self):
        category_id = self.get_valid_input("Enter category ID: ")
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM categories WHERE category_id = ?",
                       (category_id,))
            cursor.execute("DELETE FROM expenses WHERE category_id = ? AND user_id = ?",
                       (category_id, self.current_user_id))
            self.db.commit()
            print("Expense category and related expenses deleted successfully.")
        except sqlite3.IntegrityError:
            print("Failed to delete the expense category")

    def view_expenses(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * from expenses WHERE user_id = ?",
                       (self.current_user_id,))
        expenses = cursor.fetchall()
        for expense in expenses:
            print(expense)

    def view_expense_categories(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()
        for category in categories:
            print(category)

    def income_menu(self):
        while True:
            option = input('''Enter a menu option: 
                           1. Add Income
                           2. Delete Income Category
                           3. Add Income Category
                           4. Track Income
                           5. View Income Categories
                           6. Main Menu 
            ''')
            if option == '1':
                self.add_income()
            elif option == '2':
                self.delete_income_category()
            elif option == '3':
                self.add_income_category()
            elif option == '4':
                self.track_income()
            elif option == '5':
                self.view_income_categories()
            elif option == '6':
                break
            else: 
                print("Invalid input. Please try again.")

    def add_income(self):
        category_id = self.get_valid_input("Enter category ID: ")
        amount = self.get_valid_input("Enter amount: ")
        date = input("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")

        cursor = self.db.cursor()
        cursor.execute("SELECT category_id FROM income_categories where category_id = ?",
                       (category_id,))
        if cursor.fetchone() is None:
            print(f"Category ID {category_id} does not exist. Please enter valid ID.")
            return
        
        cursor.execute("INSERT OR IGNORE INTO incomes (user_id, category_id, amount, date, description) VALUES (?, ?, ?, ?, ?)",
                       (self.current_user_id, category_id, amount, date, description))
        self.db.commit()
        if cursor.rowcount == 0:
            print("Income already exists.")
        else:
            print("Income added successfully.")

    def delete_income_category(self):
        category_id = self.get_valid_input("Enter category ID: ")
        cursor = self.db.cursor()
        try:
            cursor.execute("DELETE FROM income_categories WHERE category_id = ?",
                       (category_id,))
            cursor.execute("DELETE FROM incomes WHERE category_id = ? AND user_id = ?",
                       (category_id, self.current_user_id))
            self.db.commit()
            print("Income category and related income deleted successfully.")
        except sqlite3.IntegrityError:
            print("Failed to delete income category.")

    def add_income_category(self):
        category_name = input("Enter new income category name: ")
        cursor = self.db.cursor()
        try:
            cursor.execute("INSERT OR IGNORE INTO income_categories (category_name) VALUES (?)",
                       (category_name,))
            self.db.commit()
            if cursor.rowcount == 0:
                print("Income category already exists.")
            else:
                print("Income category added successfully.")
        except sqlite3.IntegrityError:
            print("Failed to add the income category.")

    def track_income(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM incomes WHERE user_id = ?",
                       (self.current_user_id,))
        incomes = cursor.fetchall()
        for income in incomes:
            print(income)

    def view_income_categories(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM income_categories")
        categories = cursor.fetchall()
        for category in categories:
            print(category)

    def budget_calculator(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT SUM(amount) FROM incomes where user_id = ?",
                       (self.current_user_id,))
        total_income = cursor.fetchone()[0] or 0
        cursor.execute("SELECT SUM(amount) FROM expenses where user_id = ?",
                       (self.current_user_id,))
        total_expenses = cursor.fetchone()[0] or 0
        remaining_budget = total_income - total_expenses
        print(f"Total Income: {total_income}")
        print(f"Total Expenses: {total_expenses}")
        print(f"Remaining Budget: {remaining_budget}")

    def main_menu(self):
        while True:
            if not self.current_user_id:
                print('''
                      1. Register
                      2. Login
                      3. Exit
                      ''')
                option = input("Select an option: ")
                if option == '1':
                    self.register_user()
                elif option == '2':
                    self.login_user()
                elif option == '3':
                    self.exit_program()
                else:
                    print("Invalid option. Please try again.")
            else:
                option = input('''Enter a menu option:
                    1. Expense Menu
                    2. Income Menu
                    3. Budget Calculator
                    4. Logout
                    5. Exit
                ''')
            
                if option == '1':
                    self.expense_menu()
                elif option == '2':
                    self.income_menu()
                elif option == '3':
                    self.budget_calculator()
                elif option == '4':
                    self.current_user_id = None
                elif option == '5':
                    self.exit_program()
                else:
                    print("Invalid option. Please try again.")

if __name__ == "__main__":
    tracker = Budget_Tracker('data/expense_tracker.db')
    tracker.main_menu()