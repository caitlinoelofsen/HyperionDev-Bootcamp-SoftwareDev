# Create a new text file
with open('reg_form.txt', 'a') as f:

    # Ask user how many students are registering
    while True: 

        # Loop until a valid integer is input
        try:
            number_of_students = int(input("How many students are registering? "))
            break
        except ValueError:
            print("Invalid number. Please enter a whole number. ")
          
    # Loop through that number of students to obtain ID numbers
    for i in range(number_of_students):
        while True:
            try:
                id_numbers = int(input("Input student ID number: "))

                # Write ID numbers to text file
                f.write(f"Student ID number: {id_numbers} .........\n")
                break
            except ValueError:
                print("Please enter a valid ID number. ")

    # Thank the user for entering all ID numbers.             
    print("Thank you for entering all ID numbers.")


            



