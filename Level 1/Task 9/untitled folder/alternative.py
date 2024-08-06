# Converting each alternate character of user input to uppercase 

# Requesting user input
pet_name = input("What is your dog's name? ")
new_string = ""

# Indexing through length of string variable
for i in range(len(pet_name)):

    # Converting alternate characters to uppercase 
    if i % 2 == 1:
        new_string += pet_name[i].upper()
    
    else: 
        new_string += pet_name[i].lower()

# Printing user's name in a sentence    
print(f"Dang, {new_string} ate the pizza again! ") 

# Converting each alternate word of sentence to uppercase
string = f"Dang, {new_string} ate the pizza again! "

upper_words = string.split()

# Initializing a for loop to call upper() 
for i in range(len(upper_words)):

    if i % 2 == 0:
        upper_words[i] = upper_words[i].upper()

# Using join() method to concatenate the list back into a string
    final_string = " ".join(upper_words)

print(final_string)