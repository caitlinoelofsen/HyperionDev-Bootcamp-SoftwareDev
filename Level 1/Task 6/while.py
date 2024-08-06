# Declared counter variables total and count
total = 0
count = 0

# Started a while loop to process user input
while True:

    # Implemented a try except block to handle cases where user doesn't enter an integer
    try:

        # Requested users input or -1 to exit
        user_number = int(input("Please enter a number (-1 to exit): "))
         
        # Used an if statement with a condition to repeat the loop as long as user doesn't enter - 1
        if user_number != - 1:

            # Set total variable to user input and increased count variable by 1 with each user input
            total += user_number 
            count += 1     

        # Used an if statement to break the loop if user enters -1       
        if user_number == - 1:
                print(total / count)
                break
        
    except ValueError:
                  print("Invalid input. Please enter a whole number. ")

''' Used the following resource to understand how to count user input to calculate the average for this task:
https://www.quora.com/How-do-you-create-a-Python-program-that-loops-and-counts-how-many-times-the-user-entered-a-number-It-should-not-be-more-than-3 '''                