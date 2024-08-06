# Used a while loop to ensure user enters a whole number 
while True: 
        # Used try except block to catch errors
        try:

            # Requesting event times from user
            swimming = int(input("Input time for swimming in minutes. "))
            cycling = int(input("Input time for cycling in minutes. "))
            running = int(input("Input time for running in minutes. "))

            # Used break function to end the while loop if True
            break
        except Exception:
               print("Invalid input. Please enter a whole number")
    
# Calculating user's total time
total_time = swimming + cycling + running
    
# Determining which award user achieved
if total_time <= 100:
        print("Congratulations, you achieved Provinical Colours! ")
    
elif total_time > 100 and total_time <= 105:
        print("Well done, you achieved Provincial Half Colours! ")

elif total_time > 105 and total_time <= 110:
        print("You achieved a Provincial Scroll! ")

else: 
        print("You did not receive an award. ")

# Learned about input validation and how to use a while loop here https://p-kane.medium.com/input-validation-with-python-570953d5d297