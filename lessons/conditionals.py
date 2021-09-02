"""An example of conditional (if-else) statements. """

SECRET: int = 3
# This is a special kind of variable. When a var is all caps, it means the programmer does not plan on changing it.


print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

# This is a boolean, using a relational operator. All conditions are booleans
# if always relates to True in a boolean.

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wonderful day!!!")
else:
    print("Sorry, you guessed incorrectly.")
    
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed too low!")

print("Game over.")