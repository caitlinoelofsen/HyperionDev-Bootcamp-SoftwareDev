# Declaring variables to hold the sentence the code will convert
sentence = "My dog ate the pizza. "
string = ""

# Indexing through length of sentence variable
for i in range(len(sentence)):

    # Converting characters into uppercase and lowercase
    if i % 2 == 1:
        string += sentence[i].upper()
    
    else: 
        string += sentence[i].lower()

# Printing modified string    
print(string) 

# Split the original sentence into words
upper_words = sentence.split()

# Initializing a for loop to apply uppercase to every other word
for i in range(len(upper_words)):

    if i % 2 == 1:
        upper_words[i] = upper_words[i].upper()

# Joining the words back into a single string and printing output
final_string = " ".join(upper_words)
print(final_string)