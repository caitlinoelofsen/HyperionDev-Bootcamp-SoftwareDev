def find_largest_number(list_of_numbers):
    if len(list_of_numbers) == 1:  # Set base case
        return list_of_numbers[0]
    else:  # Set recursive case
        largest_num_of_list = find_largest_number(list_of_numbers[1:])
        if list_of_numbers[0] > largest_num_of_list:
            return list_of_numbers[0]
        else:
            return largest_num_of_list
print(find_largest_number([10, 13, 4, 6, 60]))
'''
I used the following resource to complete this task 
https://tinyurl.com/v2nw9vw7
'''
