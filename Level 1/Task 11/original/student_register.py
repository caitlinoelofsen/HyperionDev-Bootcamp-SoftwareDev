# Declare counter variable to count total ID numbers input
total_id_numbers = 0

# Create a new text file

with open('reg_form.txt', 'w') as f:

# Intitialise a while loop
while True:  
    
    # Ensure user only inputs integers
    try:
       
        # Ask the user how many students are registering
        number_of_students = int(input("How many students are registering? "))

        # Loop through that number of students to obtain ID numbers
        for i in range(number_of_students):
                
            '''id_numbers = int(input("Input student ID number: "))

            if range(id_numbers) != range(number_of_students):
                    id_numbers += total_id_numbers'''

                
        # Write the ID numbers to text file
        f.write(" Student ID number: " + str(id_numbers) + "  ............." + "\n")

    except ValueError: 
        print("Invalid number. Please enter a whole number. ")

        # Thank the user for entering all ID numbers
    else:
        print("Thank you for entering all ID numbers.")






            



