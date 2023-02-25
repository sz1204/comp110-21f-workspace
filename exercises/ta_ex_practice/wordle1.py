
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def main() -> None:
    """Entrypoint of game."""
    turn: int = 1
    secret: str = "codes"
    won: bool = False
    while turn < 7 and not won:
        print("=== Turn " + str(turn) + "/6 ===")
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        if guess == secret:
            won = True
        else:
            turn += 1
    if won:
        print("You won in " + str(turn) + "/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


def contains_char(answer: str, test_char: str) -> bool:
    """Tests whether test_char is found anywhere in the answer string."""
    assert len(test_char) == 1
    i: int = 0
    while i < len(answer):
        if answer[i] == test_char[0]:
            return True
        i += 1
    return False


def emojified(guess: str, answer: str) -> str:
    """Given a guess, return wordle-esque emoji string."""
    assert len(guess) == len(answer)
    i: int = 0
    contain: bool = False
    result: str = " "
    while i < len(answer):
        if answer[i] == guess[i]:
            result += GREEN_BOX
        else:
            contain = contains_char(answer, guess[i])
            if contain:
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        i += 1
    return result


def input_guess(exp_len: int) -> str:
    """Ensure guess is the right expected length."""
    guess: str = input("Enter a " + str(exp_len) + " character word: ")
    while len(guess) != exp_len:
        guess = input("That wasn’t " + str(exp_len) + " chars! Try again: ")
    return guess

    
if __name__ == "__main__":
    main()