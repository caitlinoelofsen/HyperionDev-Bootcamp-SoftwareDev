# Define a function that takes a list as an argument
def find_largest_number(numbers):
    if len(numbers) == 1: # Set base case
        return numbers[0]
    else:  # Set recursive case to find the largest number in the list
        largest_num = find_largest_number(numbers[1:]) 
        if numbers[0] > largest_num:
            return numbers [0]
        else: 
            return largest_num  

print(find_largest_number([10, 15, 60, 45, 100]))  # Call the function  

'''
I used the following resources to complete this task
https://tinyurl.com/2tf4acp4
https://tinyurl.com/4bu4drft 
'''