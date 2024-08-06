# Declare counter variable to store the star pattern
stars = "*"

# Loop from 1 to 9 to create the pattern
for i in range(1,10):

    # Print the current pattern and add a star within the first part of the loop
    if i <= 4:
       print(stars)
       stars += "*"
    
    # Using the slice operation print the second part of the loop backwards
    else:
        print(stars)
        stars = stars[:-1]

''' Used the following resource to figure out how to print the loop backwards as it was initially only printing the first part of the loop and not the second part.
https://stackoverflow.com/questions/77422605/program-for-an-upright-and-inverted-triangle-pattern-with-one-for-loop-and-if-el'''