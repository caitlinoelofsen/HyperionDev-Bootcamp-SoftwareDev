# Used input function to request user's favourite restaurant
string_fav = input("What is the name of your favourite restaurant? ")
# Requested user's favourite number
fav_no = input("What is your favourite number? ")
# Converted string into an integer
int_fav = int(fav_no)
# Printed both statements on a seperate line using two print statements
print(string_fav)
print(int_fav)
# Attempted to cast string_fav as an integer using int() function
cast_str = int(string_fav)
# Error message occured as the string contains characters that are not numerals