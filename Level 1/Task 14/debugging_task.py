# Function to print dictionary values given the keys
def print_values_of(dictionary, keys):
    for key in keys:

        # Logic Error & Runtime Error:
        # Amended the key to match the iterator variable in for loop
        print(dictionary[key]) 

# Print dictionary values from simpson_catch_phrases
simpson_catch_phrases = {"lisa": "BAAAAAART!", 
                         "bart": "Eat My Shorts!", 
                         "marge": "Mmm~mmmmm", 

                         # Syntax Error:
                         # Changed '' around value to ""
                         "homer": "d'oh!", 
                         "maggie": "(Pacifier Suck)"
                         }

# Syntax Error & Logic Error:
# Changed single quotation marks to double to match the key
# Grouped as a list to make second argument and print in correct order
print_values_of(simpson_catch_phrases, ["lisa", "bart", "homer"]) 

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

