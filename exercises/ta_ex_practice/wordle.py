"""Exercise 2: One Shot Wordle"""

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

number_of_letters: int = 0
letter: int = 0
emoji: str = ""
may_exist: int = 0
check_for_yellow: int = 0

number_of_letters = 6
secret_word: str = "python"
guess: str = input(f"What is your {number_of_letters}-letter guess? ")

while (len(guess) != number_of_letters):
    guess: str = input(f"That was not {number_of_letters} letters! Try again: ")

while letter < number_of_letters:
    if guess[letter] == secret_word[letter]:
        emoji += GREEN_BOX
    else:
        may_exist = 0
        check_for_yellow = 0
        while may_exist < number_of_letters:
            if guess[letter] == secret_word[may_exist]:
                emoji += YELLOW_BOX
                check_for_yellow = 1
            may_exist += 1
    if guess[letter] != secret_word[letter] and check_for_yellow == 0:
        emoji += WHITE_BOX 
    letter += 1
print(emoji)

if guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")