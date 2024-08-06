# Code that produces a joke with limited guesses

# Requesting user's answer to joke
print("Why do programmers prefer dark mode? " # Syntax error: missing parenthesis

correct_answer = "Because light attracts bugs!" # Logical error: including the symbol ! means the program will find the answer wrong until it is included
guess = " "
max_attempts = 3
attempts == 0 # Runtime error: variable not defined 

while guess.lower() != correct_answer.lower():
    guess = input("Guess why or type 'exit' to see the answer. ")
    attempts += 1

    if guess.lower() == "exit" # Syntax error: missing colon  
        print("The correct answer is: " + correct_answer) 
        break

    elif guess.lower() == correct_answer.lower(): 
        print("Correct! That's right. ")

    else:
        print("Nope, try again!")

if attempts == max_attempts:
    print("You have used all your guesses. ")

'''Used the following resource to understand how to make this code non-case sensitive. 
https://stackoverflow.com/questions/55728451/how-to-make-this-code-non-case-sensitive'''