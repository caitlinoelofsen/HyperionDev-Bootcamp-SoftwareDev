# Program designed to calculate total cost of user's holiday
# Functions to calculate total cost of flight, hotel and car rental
def hotel_cost(num_nights):
    return num_nights * 1300

# Assign price values to different flight options
def plane_cost(city_flight):
    if city_flight == 1:
        return 20000
    elif city_flight == 2:
        return 15000
    elif city_flight == 3:
        return 22000
    
def car_rental(rental_days):
   return rental_days * 800

def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

# Offer the user different flight options
def flight_options():
    print("Flight Options:")
    print("1 = Tokyo ")
    print("2 = London ")
    print("3 = Paris ")

print("Calculate your total holiday cost: ")
flight_options()

# Obtain user's input 
while True:
    try: 
        city_flight = int(input("Input the number for your destination city. "))

# Handle cases where user does not choose a provided flight option
        if city_flight >= 4:
            print("Please choose a flight option provided. ")
            continue

        num_nights = int(input("Enter number of nights at your hotel. "))
        rental_days = int(input("Enter number of days you require a car. "))

# Ensure user only enters integers  
    except ValueError:
        print("Please input an integer. ")
        continue
    
# Calculate the total cost of user's holiday
    total_cost = holiday_cost(hotel_cost, plane_cost, car_rental)
    print(f"Your total holiday cost is: R{total_cost:.2f}")
    break

# I used the following resource to complete this task
# https://www.programiz.com/python-programming/break-continue
