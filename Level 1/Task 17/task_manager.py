# Import libraries
import re
from datetime import datetime
import sys

def login():  # Allow user to login 
    with open('user.txt', 'r') as user_file:
        user_login_details = {}
        for line in user_file.readlines():
            username, password = line.strip().split(', ')
            user_login_details[username] = password

    while True:  # Handle cases where user details are input incorrectly
        username = input("Enter username: ")
        if username in user_login_details:
            while True:
                password = input("Enter password: ")
                if password == user_login_details[username]:
                    print("You have successfully logged in!")
                    is_admin = (username == "admin")

                    # Capture username and determine if user is admin 
                    return True, username, is_admin
                else:
                    print("Incorrect password! Please try again.")
        else: 
            print("Incorrect username. Please try again.")

# Pass username variable to register user function to check current user 
def register_user(username):  
    if username != "admin":  # Allow only admin to register new users
        print("You do not have authorization to enter new users.\n")
        return False 
    else:
        username_input = input("Enter a new username. ")

    while True:
        password_input = input("Enter the password. ")

        # Ensure password adheres to specific security standards
        password_pattern = "^[a-zA-Z0-9!@#$&()\\-`.+,/\"]*$"

        if re.match(password_pattern, password_input):
            confirmed_password = input("Enter the password again. ")
            if confirmed_password != password_input:
                print("Your passwords do not match. Please try again.")
                continue
            else:
                try:  # Write new user's login details to user text file
                    with open('user.txt', 'a') as user_file:
                        user_file.write(
                            f'{username_input}, {confirmed_password}\n')
                        print("User successfully registered.\n")
                        return True
                except FileNotFoundError:
                    print("File not found, Please make sure file exists.")
        else:
            print("Password is not valid. Please try again.")

def validate_user_date():  # Ensure user enters date in correct format
    while True:
        try:
            date_input = input("Enter the due date (yyyy-mm-dd): ")
            validated_date = datetime.strptime(date_input, '%Y-%m-%d') 
            return validated_date.date()
        except ValueError:
            print("Incorrect date format. Input YYYY-MM-DD: ")

def add_task():  # Allow user to create and assign tasks
    name_of_task = input("Enter the title of the task: ")
    name_of_asignee = input("Enter employee name: ").lower()
    date_assigned = datetime.today().date()  # Get today's date
    due_date_of_task = validate_user_date()
    description_of_task = input("Enter a description of the task: ")
    task_complete = False
    if task_complete == False:
        task_complete = "No"
    else:
        task_complete = "Yes"

    try:  # Write tasks to txt file and handle cases where file not found     
        with open('tasks.txt', 'a') as task_file:  
            task_file.write( 
            f'Task: {name_of_task}, '
            f'Assigned to: {name_of_asignee}, ' 
            f'Date assigned: {date_assigned}, '
            f'Due date: {due_date_of_task}, '
            f'Task description: {description_of_task}, '
            f'Task complete? {task_complete}\n'
        )
    except FileNotFoundError:
        print("File not found. Please make sure file exists.")

def view_all_tasks():  # Allow user to view all tasks
    print("\nAll User Tasks:\n")
    try:
        with open('tasks.txt', 'r') as task_file:
            for tasks in task_file:
                formatted_tasks = tasks.split(', ')
                for all_task_details in formatted_tasks:
                    print(all_task_details)
    except FileNotFoundError:
        print("File not found. Please make sure file exists.")

def view_my_tasks(username):  # Allow user to view their tasks
    found = False

    # Set username pattern to locate current user's tasks in text file
    username_pattern = username
    print("\nYour Assigned Tasks:\n")
    try:
        with open('tasks.txt', 'r') as task_file:
            for task in task_file:
                if username_pattern in task:
                    formatted_task = task.split(', ')
                    for user_task_details in formatted_task:
                        print(user_task_details.strip())
                    print()
                    found = True

        if not found:  # Handle cases where username is not found
            print(f'No tasks found for {username}. ')
    except FileNotFoundError:
        print("File not found. Please make sure file exists.")

def statistics():  # Allow admin user to view number of tasks and users
    try:
        with open('user.txt', 'r') as user_file:
            users = user_file.readlines()
            print("\nTotal number of users:")
            print(len(users))
    except FileNotFoundError:
        print("File not found. Please make sure file exists.")

    try:
        with open('tasks.txt', 'r') as task_file:
            tasks = task_file.readlines()
            print("\nTotal number of tasks:")
            print(len(tasks))
    except FileNotFoundError:
        print("File not found. Please make sure file exists.")

def exit_program():  # Allow user to exit the program
    print("Exiting the program...")
    sys.exit(0)

def main_menu():  # Identify the user and present the appropriate menu
    login_success, username, is_admin = login()
    if login_success:
        if is_admin:
            admin_menu(username)
        else:
            user_menu(username)

def admin_menu(username):  # Present the admin menu to admin user
    while True:
        menu = input('''\nSelect one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
st - view statistics
e - exit
: ''').lower()
    
        # Map admin user's input to corresponding function
        if menu == 'r':
            register_user(username)  
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all_tasks()
        elif menu == 'vm':
            view_my_tasks(username)
        elif menu == 'st':
            statistics()
        elif menu == 'e':
            exit_program()
        else:  # Handle invalid inputs
            print("Invalid input. Please try again.")

def user_menu(username):  # Present the user menu 
    while True: 
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

        # Map user input to corresponding function
        if menu == 'r':
            register_user(username)
        elif menu == 'a':
            add_task()
        elif menu == 'va':
            view_all_tasks()
        elif menu == 'vm':
            view_my_tasks(username)
        elif menu == 'e':
            exit_program()
        else:  
            print("Invalid input. Please try again.")

# Ensure main menu function is called only when script is run directly
if __name__ == "__main__":
    main_menu()

'''
I used the following resources to help me complete this project
https://tinyurl.com/3wpe5uzd
https://tinyurl.com/yk3s4zau
https://tinyurl.com/6wb6ubkw
https://tinyurl.com/yeyv7au7
https://tinyurl.com/bpdezv4v
https://tinyurl.com/2bwn25c6
https://tinyurl.com/3phjctjy
https://tinyurl.com/fjrkzm2d
https://tinyurl.com/3hueu772
https://tinyurl.com/2b6ppz6r
https://tinyurl.com/4epp4xj7
'''
