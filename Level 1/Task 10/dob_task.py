# Open the text file in Python
f = open('DOB.txt', 'r+' )

# Declare empty lists to contain name and birthdate data
names = []
birthdates = []

# Loop through each line of the text file
for line in f:

    # Split the lines in the text file 
    words = line.split()

    # Compile names and birthdates into seperate lists
    name = ' '.join(words[0:2])
    birthdate = ' '.join(words[2:5])

    names.append(name)
    birthdates.append(birthdate)
    
# Print the names and birthdates 
print("\nName ")
for name in names:
    print(name)

print("\nBirthdate ")
for birthdate in birthdates:
    print(birthdate)

# Close the text file 
f.close()

'''Following resources used to complete this task:
https://stackoverflow.com/questions/56962347/how-do-i-print-the-1st-word-of-each-line-in-a-txt-file
https://stackoverflow.com/questions/8546245/python-concat-string-with-list '''