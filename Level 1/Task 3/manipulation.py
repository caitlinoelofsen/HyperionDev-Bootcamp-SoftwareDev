# Asked the user for a sentence using input function
str_manip = input("Enter a sentence. ")
# Calculated the length of the string using len() function
print(len(str_manip))
# Used indexing and replace() function to find the last letter in user's sentence and replace letter with an @
last_letter = str_manip[-1]
str_rep = str_manip.replace(last_letter, "@")
print(str_rep)
# Used an extended slice to print last three characters of user's sentence backwards
print(str_manip[-1:-4:-1])
# Used indexing and concatenation to create five letter word made up of the first three, and last two characters of user's sentence
new_word = str_manip[:3] + str_manip[-2:]
print(new_word)