import sqlite3
import os
import sys

class Ebookstore:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = self.connect_db()  # Connect to the database
        self.create_table()  # Create the table if it does not exist

    def connect_db(self):
        if not os.path.exists('data'):
            os.makedirs('data')  # Create directory if it doesn't exist
        return sqlite3.connect(self.db_path)

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS book(
                   id INTEGER PRIMARY KEY,
                   title TEXT,
                   author TEXT,
                   qty INTEGER)
        ''')
        self.db.commit()
        print("Table created or already exists.")

    def initialise_books(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT COUNT (*) FROM book')
        count = cursor.fetchone()[0]

        if count == 0:
            books = [            
            (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
            (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K Rowling', 40),
            (3003, 'The Lion the Witch and the Wardrobe', 'C.S Lewis', 25),
            (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
            (3005, 'Alice in Wonderland', 'Lewis Carroll', 12)
            ]

            cursor.executemany('''INSERT INTO book(id, title, author, qty)
                               VALUES (?,?,?,?)''', books)
            self.db.commit()
            print("Books initialised.")
        else:
            print("Books already initialised.")

    # Funtion to handle cases where invalid integers are input by user
    @staticmethod
    def get_valid_int_input (prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    # Function to enter new books into the database
    def enter_book(self):
        cursor = self.db.cursor()
        id = self.get_valid_int_input('Enter new book ID: ')
        title = input('Enter book title: ')
        author = input ('Enter author: ')
        qty = self.get_valid_int_input('Enter the quantity of stock: ')

        cursor.execute('''INSERT INTO book(id, title, author, qty)
                       VALUES(?,?,?,?)''', (id, title, author, qty))
        self.db.commit()
        print(f"Book '{title}' added successfully.")
    
    # Function to update existing books in the database
    def update_book(self):
        cursor = self.db.cursor()
        book_id = self.get_valid_int_input('Enter the ID of book to update: ')

        cursor.execute('SELECT * FROM book WHERE id = ?', (book_id,))
        book = cursor.fetchone()

        if not book:
            print("Book not found.")
            return

        fields = {
            'id': ('ID number', self.get_valid_int_input),
            'title': ('book title', input),
            'author': ('author', input),
            'qty': ('quantity of stock', self.get_valid_int_input)
        }

        updates = {}
        for field, field_name, field_input in fields:
            prompt = (f'Do you want to update the {field_name}? (Yes/No): ')
            if input(prompt).strip().lower() == 'yes':
                updates[field] = field_input(f'Update {field_name}: ')

        if updates:
            update_fields = ", ".join([f"{k} = ?" for k in updates.keys()])
            update_values = list(updates.values())
            update_values.append(book_id)
            cursor.execute(f'''UPDATED book SET {update_fields} WHERE id = ?'''
                           , update_values)
            self.db.commit()
            print("Book updated successfully.")
        else:
            print("No updates made.")

    # Function to delete a book from the database
    def delete_book(self):
        cursor = self.db.cursor()
        id = self.get_valid_int_input('Enter the ID number of the book: ')
        cursor.execute('''DELETE FROM book where id = ?''',(id,))
        self.db.commit()
        print("Book successfully deleted.")

    # Function to search for a book in the database using the id or title
    def search_books(self):
        cursor = self.db.cursor()
        method = input('Search using title or id? ')

        if method == 'title':
            title = input('Enter the book title: ')
            cursor.execute('''SELECT * FROM book WHERE title LIKE ?''',
                       ('%' + title + '%',))
            results  = cursor.fetchall()
            if results:
                for row in results:
                    print(row)
            else:
                print("No book found with that title.")
            input("Press enter to return to main menu...")

        elif method == 'id':
            id = self.get_valid_int_input('Enter the ID number of the book: ')
            cursor.execute('''SELECT * FROM book WHERE id = ?''', (id,))
            results = cursor.fetchall()
            if results:
                for row in results:
                    print(row)
            else:
                print("No book found with that id number.")
            input("Press enter to return to the main menu...")
        else:
            print("Invalid input. Please try again.")
            input("Press enter to return to the main menu...")

    # Function to close the database connection and exit the program
    def exit_program(self):
        print("Exiting the program...")
        self.db.close()
        sys.exit(0)

    def main_menu(self):  # Allow user to navigate program options
        while True:
            option = input('''Enter a menu option: 
              1. Enter book
              2. Update book
              3. Delete book
              4. Search books
              0. Exit
              ''')
      
            if option == '1':
                self.enter_book()
            elif option == '2':
                self.update_book()
            elif option == '3':
                self.delete_book()
            elif option == '4':
                self.search_books()
            elif option == '0':
                self.exit_program()
            else:
                print('Invalid input, please try again.')

if __name__ == "__main__":

    try:

        # Initialise the Ebookstore with the database path
        ebookstore = Ebookstore('data/ebookstore')

        # Initialsie the books if they have not been added yet
        ebookstore.initialise_books()

        # Start the main menu 
        ebookstore.main_menu()

    except sqlite3.IntegrityError as e:
        print(f"Integrity error occured: {e}")
    except sqlite3.OperationalError as e:
        print(f"Operational error occured as {e}")
    except sqlite3.ProgrammingError as e:
        print(f"Programming error occured as {e}")
    except sqlite3.DatabaseError as e:
        print(f"Database error occuredL as {e}")
    except Exception as e:
        print(f"An unexpected error occured: as {e}")

    finally:
    # Ensure database connection is closed
        if ebookstore.db:
            ebookstore.db.close()
'''
I used the following resources to complete this task:
https://tinyurl.com/msj5jtkj
https://tinyurl.com/yt59baut 
https://tinyurl.com/yw6wadue 
https://tinyurl.com/4c2xv925
'''
