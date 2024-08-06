# Create Email class
class Email():

    has_been_read = False  # Set has been read class variable to False

    # Initialise the constructor with three arguments
    def __init__(self, email_address, subject_line, email_content):

        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):  # Change read status of emails
        self.has_been_read = True

inbox_list = []

def populate_inbox():  # Create 3 sample emails and add to the Inbox list. 

    email_1 = Email("mentor@HyperionDev.com", 
                    "Welcome to HyperionDev!", 
                    ("Welcome to HyperionDev. " 
                    "We are excited to get you started with your course."
                    " \n\nBest regards,"
                    " \nHyperionDev Mentors")
    )
    email_2 = Email("Tammy@HyperionDev.com", 
                    "Great work on the bootcamp!",
                    ("Great work on the bootcamp. You received above grade " 
                    "average. \nBe sure to take a look at our career coaching " 
                    "resources and get in touch with the team."
                    " \n\nKind regards,"
                    " \nTammy")
    )
    email_3 = Email("kelly@HyperionDev.com", 
                    "Your excellent marks!", 
                    ("Well done on your final task! \nYour marks were " 
                    "outstanding. \nWe want to commend you on the high " 
                    "standard of work that you submitted."
                    " \n\nKind regards,"
                    " \nKelly")
    )

    inbox_list.extend([email_1, email_2, email_3])

# Print the email subject lines and the corresponding number
def list_emails():  
    for index, email in enumerate(inbox_list, start=0):
        print(f"{index}. {email.subject_line}")

def read_email():  # Allow users to view selected emails
    try:
        index = int(input("Input the number of the email you want to read. "))
        if 0 <= index < len(inbox_list):
            email = inbox_list[index]
            email.mark_as_read()  # Mark opened emails as read
            print("\n" "From: " + email.email_address)
            print("Subject: " + email.subject_line)
            print("\n" + email.email_content)
            print("-" * 40)
        else: 
            print("Email not found.")
    except ValueError:  # Handle cases where user enters non integer
        print("Invalid input. Please enter a valid number. ")

def main():  # Present program menu to users
    populate_inbox()
    menu = True

    while menu:
        try: 
            user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

            if user_choice == 1:
                list_emails()
                read_email()

            elif user_choice == 2:
                unread = False
                for index, email in enumerate(inbox_list):
                    if not email.has_been_read:
                        print(f"{index}. {email.subject_line} - Unread")
                        unread = True
                if not unread:  # Handle cases of no unread emails
                    print("No unread emails.")

            elif user_choice == 3:
                print("Exiting the program...")
                menu = False  # Break the loop and exit the program

            else:
                print("Menu option not found. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a number for your choice.")

if __name__ == "__main__":
    main()
