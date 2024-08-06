import sqlite3
import os

# Ensure data directory exists or create it
if not os.path.exists('data'):
    os.makedirs('data')

# Use absolute path so script can run from different locations/environments
db_path = os.path.abspath('data/student_db')  

db = None

try:
    # Connect to the SQLite database
    db = sqlite3.connect(db_path)
    cursor = db.cursor()  # Get a cursor object
    
    # Create the table if it doesn't already exist
    cursor.execute('''
               CREATE TABLE IF NOT EXISTS python_programming(
                    id INTEGER PRIMARY KEY, 
                    name TEXT, 
                    grade INTEGER)
    ''')
    db.commit()

    # Clear the table before adding new records 
    cursor.execute('DELETE FROM python_programming')
    db.commit()

    # Insert all student details into python_programming table
    students = [
        (55, 'Carl Davis', 61),
        (66, 'Dennis Fredrickson', 88),
        (77, 'Jane Richards', 78),
        (12, 'Peyton Sawyer', 45),
        (2, 'Lucas Brooke', 99)
    ]

    cursor.executemany('''INSERT INTO python_programming(id, name, grade)
                   VALUES (?,?,?)''',students)

    db.commit()

    # Select all records that match between 60 and 80 
    grade_lower_bound = 60 
    grade_upper_bound = 80
    cursor.execute('''SELECT * FROM python_programming WHERE grade 
                   BETWEEN ? AND ?''', (grade_lower_bound, grade_upper_bound))

    results = cursor.fetchall()
    for row in results:
        print(row)

    # Update the grade of the student with id 55
    grade = 65
    student_id = 55
    cursor.execute('''UPDATE python_programming SET grade = ? WHERE
               id = ?''', (grade, student_id))

    db.commit()

    # Delete the student with id 66
    student_id = 66
    cursor.execute('''DELETE FROM python_programming where id = ?''', 
                   (student_id,))

    db.commit()

    # Update the grades of all students with id greater than 55 to 80
    cursor.execute('''UPDATE python_programming SET grade = 80 where id 
               > 55''')

    db.commit()

    # Select and print all records from python_programming table
    cursor.execute('''SELECT * FROM python_programming''')
    results = cursor.fetchall()
    for row in results:
        print(row)

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
    # Close the database connection
    if db:
        db.close()

'''
I used the following resources to complete the task:
https://acesse.dev/sQoEH
https://acesse.dev/AMLir 
https://l1nq.com/2tsjw
'''