# Requesting user's full name using input function
name = input("Please input your full name. ")

# Checking that user did not leave the answer blank
if len(name) == 0: 
    print("You haven't entered anything. Please enter your full name.")

# Making sure that the user input their name and surname
elif len(name) < 4: 
    print("You have entered less than 4 characters. Please make sure that you have entered your name and surname.")

# Ensuring the user input only their full name 
elif len(name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

# Thanking the user for entering their full name 
else: 
    print("Thank you for entering your name.")