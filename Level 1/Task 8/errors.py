# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.


print("Welcome to the error program") # Syntax Error: Missing parenthesis in call to 'print'

print("\n") # Syntax Error: Indentation error and missing parenthesis on call to 'print'

# Variables declaring the user's age, casting the str to an int, and printing the result

age_Str = "24" # Syntax error: Indentation error | Runtime error: Cannot cast characters to an integer
age = int(age_Str) # Syntax error: Indentation error and age_Str not defined because of incorrect operand
print("I'm " + str(age) + " years old.") # Syntax error: Indentation error | Runtime error: Cannot concatenate str and int

# Variables declaring additional years and printing the total years of age

years_from_now = "3.5" # Syntax error: Indentation error | # Logical error: 3 years equals 324 months not 330 months
total_years = age + float(years_from_now) # Syntax error: Indentation error | Runtime error: Cannot concatenate str and int

# Logical error: answer_years printing str instead of int. Removed inverted commas and cast total years as a string 
print("The total number of years: " + str(total_years)) # Syntax error: Missing parenthesis on call to 'print' | Runtime error: Cannot concatenate str and float

# Variable to calculate the total amount of months from the total amount of years and printing the result

total_months = total_years * 12 # Syntax error: Calling incorrect variable 

print("In 3 years and 6 months, I'll be " + str(total_months) + " months old") # Syntax error: Missing parenthesis on call to 'print' | Runtime error: Cannot concatenate str and float

#HINT, 330 months is the correct answer

