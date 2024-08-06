# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion" # Syntax error: value not defined as it is not a string 
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth. " # Runtime error: incomplete f string. | Logical error: incorrect order of variables

print(full_spec) # Syntax error: Missing parenthisis on 'print' statement

