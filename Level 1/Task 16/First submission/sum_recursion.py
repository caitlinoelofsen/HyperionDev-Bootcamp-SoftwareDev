# Define a function that takes a list and index as arguments
def sum_up_to_index(list, index):
    if len(list) == 0:  # Set base case
        return 0
    if index == 0:  # Set recursive cases
            return list[0]

    # Add first element of list plus all other elements up to given index
    else:   
        return list[0] + sum_up_to_index(list[1:], index - 1)

result = sum_up_to_index([2, 5, 6, 7, 6], 1) # Call function
print(result)

'''
I used the following resource to complete this task
https://www.youtube.com/watch?v=-Vq0bJf7GP4
'''
