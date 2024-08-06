import sqlite3
import os
import sys
from datetime import datetime

class DatabaseConnection:
    def __init__(self, db_path):

        # Initialise the DatabaseConnection with the path to database
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

class Budget_Tracker:
    def __init__(self, db_path):
        self.db_path = db_path

        # Call methods to create necessary tables
        self.create_users_table()
        self.create_expense_categories_table()
        self.create_income_categories_table()
        self.create_budget_table()
        self.create_expenses_table()
        self.create_income_table()
        self.create_goals_table()

        # Initialise variable to keep track of current user
        self.current_user_id = None

    # Create users table
    def create_users_table(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS users(
                        user_id INTEGER PRIMARY KEY,
                        username TEXT,
                        email TEXT,
                        password TEXT
                    )
                ''')
                conn.commit()
            except sqlite3.OperationalError as e: 
                print(f"SQL syntax error: {e}")
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    # Create expense categories table
    def create_expense_categories_table(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try: 
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS expense_categories(
                        category_id INTEGER PRIMARY KEY,
                        category_name TEXT
                    )
                ''')
                conn.commit()
            except sqlite3.OperationalError as e: 
                print(f"SQL syntax error: {e}")
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    # Create income categories table
    def create_income_categories_table(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try: 
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS income_categories(
                        category_id INTEGER PRIMARY KEY,
                        category_name TEXT
                    )
                ''')
                conn.commit()
            except sqlite3.OperationalError as e: 
                print(f"SQL syntax error: {e}")
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    # Create budget table
    def create_budget_table(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS budgets(
                        budget_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        category_id INTEGER,
                        category_type TEXT CHECK(category_type IN 
                        ('income', 'expense')),
                        budget_amount REAL NOT NULL,
                        start_date DATE NOT NULL,
                        end_date DATE NOT NULL,
                        FOREIGN KEY(user_id) REFERENCES users(user_id),
                        FOREIGN KEY(category_id) REFERENCES expense_categories
                        (category_id),
                        FOREIGN KEY(category_id) REFERENCES income_categories
                        (category_id)
                    )
                ''')
                conn.commit()
            except sqlite3.OperationalError as e: 
                print(f"SQL syntax error: {e}")
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    # Create expenses table
    def create_expenses_table(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS expenses(
                        expense_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        category_id INTEGER,
                        amount REAL NOT NULL,
                        date DATE NOT NULL,
                        description TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(user_id),
                        FOREIGN KEY(category_id) REFERENCES expense_categories
                        (category_id)
                    )
                ''')
                conn.commit()
            except sqlite3.OperationalError as e: 
                print(f"SQL syntax error: {e}")
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    # Create incomes table
    def create_income_table(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS incomes(
                        income_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        category_id INTEGER,
                        amount REAL NOT NULL,
                        date DATE NOT NULL,
                        description TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(user_id),
                        FOREIGN KEY(category_id) REFERENCES income_categories
                        (category_id)
                    )
                ''')
                conn.commit()
            except sqlite3.OperationalError as e: 
                print(f"SQL syntax error: {e}")
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    # Create goals table
    def create_goals_table(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS goals(
                        goal_id INTEGER PRIMARY KEY,
                        user_id INTEGER,
                        category_type TEXT CHECK(category_type IN ('income', 
                        'expense')),
                        category_id INTEGER,
                        goal_amount REAL NOT NULL,
                        start_date DATE NOT NULL,
                        end_date DATE NOT NULL,
                        description TEXT,
                        FOREIGN KEY(user_id) REFERENCES users(user_id),
                        FOREIGN KEY(category_id) REFERENCES 
                        expense_categories(category_id),
                        FOREIGN KEY(category_id) REFERENCES 
                        income_categories(category_id)
                    )
                ''')
                conn.commit()
            except sqlite3.OperationalError as e: 
                print(f"SQL syntax error: {e}")
            except sqlite3.Error as e:
                print(f"Database error: {e}")

    # Get valid integer or float input from users
    @staticmethod
    def get_valid_number(prompt):
        while True:
            try:
                value = float(input(prompt))
                if value.is_integer():
                    return int(value)
                else:
                    return value
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Get valid date input from users
    @staticmethod
    def get_valid_date(prompt):
        while True:
            date_str = input(prompt)
            try:
                valid_date = datetime.strptime(date_str, "%Y-%m-%d")
                return valid_date.date()
            except ValueError:
                print('''Invalid date format. Please enter a date in 
                    YYYY-MM-DD format.''')
    
    # Allow users to register a profile
    def register_user(self):
        username = input("Enter username: ")
        email = input("Enter email address: ")
        password = input("Enter password: ")
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''INSERT INTO users (username, email, password) 
                    VALUES (?, ?, ?)''', (username, email, password))
                conn.commit()
                print("User successfully registered.")
            except sqlite3.OperationalError as e:
                print(f"Operational Error: {e}")

    # Allow user to login and handle user input errors
    def login_user(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''SELECT user_id FROM users WHERE email = ? AND
                        password = ?''', (email, password))
                user = cursor.fetchone()
                if user:
                    self.current_user_id = user[0]
                    print("Login successful.")
                else:
                    print("Invalid email or password.")
            except sqlite3.DatabaseError as e:
                print(f"Database Error: {e}")

    # Allow users to quit the program
    def exit_program(self):
        print("Exiting program...")
        sys.exit(0)

    # Present user with expense menu
    def expense_menu(self):
        while True:
            option = input('''Enter a menu option:
                1. Add New Expense
                2. Update Expense Amount
                3. Add Expense Category
                4. Delete Expense Category
                5. View Expenses
                6. View Expense Categories
                7. Return to Main Menu
            ''')

            # Map user input to corresponding function
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

    # Allow users to add a new expense
    def add_new_expense(self):
        category_id = self.get_valid_number("Enter category ID: ")
        amount = self.get_valid_number("Enter amount: ")
        date = self.get_valid_date("Enter date (YYYY-MM-DD): ")
        description = input("Enter description: ")

        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                # Ensure expense category exists
                cursor.execute('''SELECT category_id FROM expense_categories 
                            WHERE category_id = ?''', (category_id,))
                if cursor.fetchone() is None:
                    print(f'''Category ID {category_id} does not exist. Please 
                    try again''')
                    return
        
                cursor.execute('''INSERT OR IGNORE INTO expenses (user_id, 
                            category_id, amount, date, description) VALUES 
                            (?, ?, ? , ?, ?)''', (self.current_user_id, 
                            category_id, amount, date, description))
                conn.commit()

                # Check if expense already exists
                if cursor.rowcount == 0:
                    print("Expense already exists.")
                else:
                    print("Expense successfully added.")
            except sqlite3.IntegrityError as e:
                print(f"Integrity Error: {e}")

    # Allow user to update expense amount
    def update_expense_amount(self):
        expense_id = self.get_valid_number("Enter expense ID: ")
        new_amount = self.get_valid_number("Enter new amount: ")
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''UPDATE expenses SET amount = ? WHERE expense_id
                        = ? AND user_id = ?''', (new_amount, expense_id, 
                        self.current_user_id))
                conn.commit()
                if cursor.rowcount == 0:
                    print("No expense found with given ID. Please try again.")
                else:
                    print("Expense amount updated successfully.")
            except sqlite3.OperationalError as e:
                print(f"Operational Error: {e}")

    # Allow user to add expense categories
    def add_expense_category(self):
        category_name = input("Enter new expense category name: ")
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''INSERT OR IGNORE INTO expense_categories
                            (category_name) VALUES (?)''', (category_name,))
                conn.commit()
                if cursor.rowcount == 0:
                    print("Expense category already exists.")
                else:
                    print("Expense category added successfully.")
            except sqlite3.IntegrityError as e:
                print(f"Integrity Error: {e}")

    # Allow user to delete expense categories and related expenses
    def delete_expense_category(self):
        category_id = self.get_valid_number("Enter expense category ID: ")
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try: 
                cursor.execute('''DELETE FROM expense_categories WHERE 
                        category_id = ?''', (category_id,))
                cursor.execute('''DELETE FROM expenses WHERE category_id = ? AND
                        user_id = ?''', (category_id, self.current_user_id))
                conn.commit()
                print("Expense category and related expenses deleted successfully.")
            except sqlite3.OperationalError as e:
                print(f"Operational Error: {e}")

    # Allow user to view all of their expenses
    def view_expenses(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                        SELECT 
                            expenses.expense_id,
                            users.username,
                            expense_categories.category_name,
                            expenses.amount,
                            expenses.date,
                            expenses.description
                        FROM
                            expenses
                        JOIN 
                            users ON expenses.user_id = users.user_id
                        JOIN
                            expense_categories ON expenses.category_id = 
                            expense_categories.category_id
                        WHERE
                            expenses.user_id = ?
                        ''', (self.current_user_id,))
                expenses = cursor.fetchall()
                if not expenses:
                    print("No expenses found.")
                for expense in expenses:
                    (expense_id, username, category_name, amount, date, 
                    description) = expense
                    print(f"Expense ID: {expense_id}")
                    print(f"Username: {username}")
                    print(f"Category: {category_name}")
                    print(f"Amount: {amount}")
                    print(f"Date: {date}")
                    print(f"Description: {description}")
                    print(f"-" * 40)
            except sqlite3.DatabaseError as e:
                print(f"Database Error: {e}")

    # Allow user to view all expense categories
    def view_expense_categories(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM expense_categories")
                categories = cursor.fetchall()
                for category in categories:
                   print(category)
            except sqlite3.DatabaseError as e:
                print(f"Database Error: {e}")

    # Present user with income menu
    def income_menu(self):
        while True:
            option = input('''Enter a menu option:
                1. Add Income
                2. Update Income Amount
                3. Add Income Category
                4. Delete Income Category
                5. View Income
                6. View Income Categories
                7. Return to Main Menu
            ''')
            if option == '1':
                self.add_income()
            elif option == '2':
                self.update_income_amount()
            elif option == '3':
                self.add_income_category()
            elif option == '4':
                self.delete_income_category()
            elif option == '5':
                self.view_income()
            elif option == '6':
                self.view_income_categories()
            elif option == '7':
                break
            else: 
                print("Invalid option. Please try again.")

    # Allow users to add new income
    def add_income(self):
        category_id = self.get_valid_number("Enter category ID: ")
        amount = self.get_valid_number("Enter amount: ")
        date = self.get_valid_date("Enter date (YYYY-MM-DD): ")
        description = ("Enter description: ")

        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                # Check if income category exists 
                cursor.execute('''SELECT category_id FROM income_categories WHERE
                        category_id = ?''', (category_id,))
                if cursor.fetchone() is None:
                    print(f'''Category ID {category_id} does not exist. Please 
                    try again.''')
                    return
        
                cursor.execute('''INSERT OR IGNORE INTO incomes (user_id, 
                        category_id, amount, date, description) VALUES 
                        (?, ?, ? ,?, ?)''', (self.current_user_id, category_id, 
                        amount, date, description))
                conn.commit()

                # Check if income already exists
                if cursor.rowcount == 0:
                    print("Income already exists.")
                else:
                    print("Income successfully added.")
            except sqlite3.IntegrityError as e:
                print(f"Integrity Error: {e}")

    # Allow users to update income
    def update_income_amount(self):
        income_id = self.get_valid_number("Enter income ID: ")
        new_amount = self.get_valid_number("Enter new amount: ")
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''UPDATE incomes SET amount = ? WHERE income_id = ?
                            AND user_id = ?''', (new_amount, income_id, 
                            self.current_user_id))
                conn.commit()
                if cursor.rowcount == 0:
                    print("No income found with given ID. Please try again.")
                else:
                    print("Income amount updated successfully.")
            except sqlite3.OperationalError as e:
                print(f"Operational Error: {e}")

    # Allow users to add income category
    def add_income_category(self):
        category_name = input("Enter new income category name: ")
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''INSERT OR IGNORE INTO income_categories
                            (category_name) VALUES (?)''', (category_name,))
                conn.commit()
                if cursor.rowcount == 0:
                    print("Income category already exists.")
                else:
                    print("Income category successfully added.")
            except sqlite3.IntegrityError as e:
                print(f"Integrity Error: {e}")

    # Allow user to delete income category
    def delete_income_category(self):
        category_id = self.get_valid_number("Enter income category ID: ")
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''DELETE FROM income_categories WHERE category_id 
                            = ?''', (category_id,))
                cursor.execute('''DELETE FROM incomes WHERE category_id = ? AND 
                            user_id = ?''', (category_id, self.current_user_id))
                conn.commit()
                print("Income category and related incomes deleted successfully.")
            except sqlite3.OperationalError as e:
                print(f"Operational error: {e}")

    # Allow user to view income
    def view_income(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''
                        SELECT 
                            incomes.income_id,
                            users.username,
                            income_categories.category_name,
                            incomes.amount,
                            incomes.date,
                            incomes.description
                        FROM
                            incomes
                        JOIN
                            users ON incomes.user_id = users.user_id
                        JOIN
                            income_categories ON incomes.category_id = 
                            income_categories.category_id
                        WHERE
                            incomes.user_id = ?
                    ''', (self.current_user_id,))
                incomes = cursor.fetchall()
                if not incomes:
                    print("No incomes found.")
                for income in incomes:
                    (income_id, username, category_name, amount, date, 
                    description) = income
                    print(f"Income ID: {income_id}")
                    print(f"Username: {username}")
                    print(f"Category: {category_name}")
                    print(f"Amount: {amount}")
                    print(f"Date: {date}")
                    print(f"Description: {description}")
                    print("-" * 40)
            except sqlite3.DatabaseError as e:
                print(f"Database Error: {e}")

    # Allow user to view income categories
    def view_income_categories(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT * FROM income_categories")
                categories = cursor.fetchall()
                for category in categories:
                    print(category)
            except sqlite3.DatabaseError as e:
                print(f"Database Error: {e}")

    # Present budget tools to users
    def budget_tools(self):
        while True:
            option = input('''Enter budget tool option: 
                1. Budget Calculator
                2. Set Budget for Category
                3. View Budget for Category
                4. Set Financial Goals
                5. View Progress towards Financial Goals
                6. Return to Main Menu
            ''')
            if option == '1':
                self.budget_calculator()
            elif option == '2':
                self.set_category_budget()
            elif option == '3':
                self.view_category_budget()
            elif option == '4':
                self.set_financial_goals()
            elif option == '5':
                self.view_goals_progress()
            elif option == '6':
                break
            else: 
                print("Invalid option. Please try again.")

    # Calculate user's remaining budget using total income and expenses
    def budget_calculator(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
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
            except sqlite3.OperationalError as e:
                print(f"Operational Error: {e}")

    # Allow users to set category budget
    def set_category_budget(self):
        category_id = self.get_valid_number("Enter income or expense category ID: ")
        category_type = input("Enter category type (income/expense): ").strip().lower()

        # Handle invalid category type inputs
        if category_type not in ['income', 'expense']:
            print("Invalid category type. Please try again.")
            return
        budget_amount = self.get_valid_number("Enter budget amount: ")
        start_date = self.get_valid_date("Enter start date (YYYY-MM-DD): ")
        end_date = self.get_valid_date("Enter end date (YYYY-MM-DD): ")

        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                # Select income or expenses categories from database
                if category_type == 'expense':
                    cursor.execute('''SELECT category_id FROM expense_categories
                                WHERE category_id = ?''', (category_id,))
                else:
                    cursor.execute('''SELECT category_id FROM income_categories
                                WHERE category_id = ?''', (category_id,))

                # Handle cases where invalid category ID is input by user
                if cursor.fetchone() is None:
                    print(f'''Category ID {category_id} does not exist. Please 
                    try again.''')
                    return

                cursor.execute('''INSERT OR REPLACE INTO budgets
                            (user_id, category_id, category_type, budget_amount, 
                            start_date, end_date) VALUES (?, ?, ?, ?, ?, ?)''',
                            (self.current_user_id, category_id, category_type, 
                            budget_amount, start_date, end_date))
                conn.commit()
                print("Budget set successfully.")
            except sqlite3.IntegrityError as e:
                print(f"Integrity Error: {e}")

    # Allow user to view category budgets
    def view_category_budget(self):
        category_id = self.get_valid_number("Enter income or expense category ID: ")
        category_type = input("Enter category type (income/expense): ").strip().lower()
        if category_type not in ['income', 'expense']:
            print("Invalid category type. Please try again.")
            return

        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                # Select income or expenses categories from database
                if category_type == 'expense':
                    cursor.execute('''SELECT category_id FROM expense_categories
                                WHERE category_id = ?''', (category_id,))
                else:
                    cursor.execute('''SELECT category_id FROM income_categories
                                WHERE category_id = ?''', (category_id,))

                if cursor.fetchone() is None:
                    print(f'''Category ID {category_id} does not exist. Please 
                    try again.''')
                    return

                # Retrieve and display the budget for the selected category
                cursor.execute('''SELECT budget_amount, start_date, end_date 
                            FROM budgets WHERE category_id = ? AND category_type 
                            = ? AND user_id = ?''', (category_id, category_type,
                            self.current_user_id))
                budget = cursor.fetchone()
                if budget is None:
                    print(f"No budget found for category ID {category_id}.")
                else:
                    budget_amount, start_date, end_date = budget
                    print(f"Budget for {category_id} ({category_type}):")
                    print(f"   Amount: {budget_amount}")
                    print(f"   Start Date: {start_date}")
                    print(f"   End Date: {end_date}")
            except sqlite3.DatabaseError as e:
                print(f"Database Error: {e}")

    # Allow user to set financial goals
    def set_financial_goals(self):
        category_id = self.get_valid_number("Enter category ID: ")
        category_type = input("Enter category type (income/expense): ").strip().lower()
        if category_type not in ['income', 'expense']:
            print("Invalid category type. Please try again.")
            return

        # Get user goal input
        goal_amount = self.get_valid_number("Enter goal amount: ")
        start_date = self.get_valid_date("Enter start date (YYYY-MM-DD): ")
        end_date = self.get_valid_date("Enter end date (YYYY-MM-DD): ")
        description = input("Enter goal description: ")

        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''INSERT OR IGNORE INTO goals 
                        (user_id, category_type, category_id, goal_amount, 
                        start_date, end_date, description) VALUES 
                        (?, ?, ?, ?, ?, ?, ?)''', (self.current_user_id, 
                        category_type, category_id, goal_amount, start_date, 
                        end_date, description))
                conn.commit()
                print("Financial goal set successfully.")
            except sqlite3.IntegrityError as e:
                print(f"Integrity Error: {e}")

    # Allow user to view progress towards financial goals
    def view_goals_progress(self):
        with DatabaseConnection(self.db_path) as conn:
            cursor = conn.cursor()
            try:
                cursor.execute('''SELECT goal_id, category_type, category_id, 
                        goal_amount, start_date, end_date, description FROM goals 
                        WHERE user_id = ?''', (self.current_user_id,))
                goals = cursor.fetchall()
                if not goals:
                    print("No financial goals found.")
                    return

                for goal in goals:
                    (goal_id, category_type, category_id, goal_amount, start_date, 
                    end_date, description) = goal
                    if category_type == 'expense':
                        cursor.execute('''SELECT SUM(amount) FROM expenses WHERE
                                user_id = ? AND category_id = ? AND date BETWEEN
                                ? AND ?''', (self.current_user_id, category_id,
                                start_date, end_date))
                    else:
                        cursor.execute('''SELECT SUM(amount) FROM incomes WHERE
                                user_id = ? AND category_id = ? AND date BETWEEN
                                ? AND ?''', (self.current_user_id, category_id,
                                start_date, end_date))
            
                    actual_amount = cursor.fetchone()[0] or 0

                    # Calculate progress percentage
                    if goal_amount != 0:
                        progress_percentage = (actual_amount / goal_amount) * 100 
                    else:
                        progress_percentage = 0

                    print(f"Goal ID: {goal_id}")
                    print(f"   Description: {description}")
                    print(f"   Category Type: {category_type}")
                    print(f"   Goal Amount: {goal_amount}")
                    print(f"   Actual Amount: {actual_amount}")
                    print(f"   Progress: {progress_percentage:.2f}%")
                    print(f"   Start Date: {start_date}")
                    print(f"   End Date: {end_date}\n")
            except sqlite3.DatabaseError as e:
                print(f"Database Error: {e}")

    # Present main menu to user
    def main_menu(self):
        while True:

            # Enable new users to register or existing users to login
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
                    3. Budget Tools
                    4. Logout
                    5. Exit
                ''')

                if option == '1':
                    self.expense_menu()
                elif option == '2':
                    self.income_menu()
                elif option == '3':
                    self.budget_tools()
                elif option == '4':
                    self.current_user_id = None
                    print("Successfully Logged Out.")
                elif option == '5':
                    self.exit_program()
                else:
                    print("Invalid option. Please try again.")

if __name__ == "__main__":

    # Define the absolute path for the database
    db_path = os.path.abspath('data/expense_income_tracker.db')

    # Create an instance of Budget_Tracker with specified database path
    tracker = Budget_Tracker(db_path)
    tracker.main_menu() # Start the main menu loop to interact with user

'''
I created seperate menus for this task to ensure I covered all requirements 
specified in the instructions. The example menu provided did not cover 
requirements such as "Delete income or expense categories". 
'''

'''
I used the following resources to complete this task:
https://tinyurl.com/ms6ubee9
https://tinyurl.com/zwe53xvs
https://tinyurl.com/5n8sptp8
https://tinyurl.com/mdw5wz4u
https://tinyurl.com/ykw4x2z3
'''
