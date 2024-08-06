class Course:  # Create Course class
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"

    def contact_details(self):
        print("Please contact us by visiting", self.contact_website)

    def head_office_location(self):
        print("Head office location: Cape Town")

class OOP_Course(Course):  # Create subclass for OOP Course
    def __init__(self):  # Initialise description and trainer variables
        self.description = "OOP Fundamentals"
        self.trainer = "Mr Anon A. Mouse"

    def trainer_details(self):  # Print the course details
        print(f"Course Description: {self.description} | "
              f"Taught by {self.trainer}.")

    def show_course_id(self):  # Create a method to print the course ID
            course_id = "#12345"
            print("Course ID Number: " + course_id)

# Create an object of the subclass and call the methods
course_1 = OOP_Course()
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()
course_1.head_office_location()  # Print head office location
