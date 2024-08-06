# Create functions that allow user to preform calculations 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:  # Handle zero division cases
        return "Error! Cannot divide by zero. "
    return x / y 

def operands():
    print("Select your operand. ")
    print("1: + ")
    print("2: - ")
    print("3: * ")
    print("4: / ")

while True:
    operands()

    # Determine the operand required for the calculation
    operand = input("Input operand choice (1, 2, 3, 4) ")
    if operand not in ('1', '2', '3', '4'):
        print("Please input option (1, 2, 3, 4)")
        continue

    while True:
        try:
            num_1 = int(input("Input first number. "))
            num_2 = int(input("Input second number. "))
            break  # Exit inner loop if inputs are valid                   
        except ValueError:  # Ensure user only inputs numbers 
            print("Please input an integer. ")
        continue   
        
    # Calculate user's input for each operand
    if operand == '1':
        result = f'{num_1} + {num_2} = {num_1 + num_2}'            
    elif operand == '2':
        result = f'{num_1} - {num_2} = {num_1 - num_2}'               
    elif operand == '3':
        result = f'{num_1} * {num_2} = {num_1 * num_2}'
    elif operand == '4':
        result = (f'{num_1} / {num_2} = {num_1 / num_2}')

    print(result)
    try:
            
        # Record all user's calculations in a seperate file
        with open('equations.txt', 'a') as equations_file:
            equations_file.write(result + "\n")
    except FileNotFoundError:  # Handle cases where file is not found
            print("File not found. Please make sure file exists.")  

    # Print all of user's previous calculations upon request
    choice = input("Print previous calculations? (Yes/No): ")
    if choice.lower() == "yes":
        with open("equations.txt", "r") as equations_file:
            print("Previous Equations: ")
            for line in equations_file:
                print(line.strip())
            
    else: 
        print("Thank you for using the calculator app. ")

'''
I used the following resources to complete this task:
https://www.programiz.com/python-programming/examples/calculator
https://stackoverflow.com/questions/61649791/how-to-prevent-division-by-zero-exception
https://medium.com/@ewho.ruth2014/python-errors-and-exceptions-a-comprehensive-guide-to-handling-errors-and-exceptions-in-python-3e6bf9381f71
'''
                    