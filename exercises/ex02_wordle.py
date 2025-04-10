"""EX02 -  Wordle"""

__author__ = "730748060"


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Will return True if the single character of the second string is found at a index of the first string."""
    assert len(char_guess) == 1, f"len('{char_guess}') is not 1"

    index: int = 0
    while len(secret_word) > index:
        if secret_word[index] == char_guess:
            return True
        index += 1
    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Returns the emoji with the color corresponding to the result of the guess."""
    assert len(guess) == len(secret)

    color: str = ""  # empty string where emojis are added
    index: int = 0
    while index < len(guess):
        if guess[index] == secret[index]:
            color += GREEN_BOX  # Letter is correct and in the correct position
        elif contains_char(secret, guess[index]):
            color += YELLOW_BOX  # Letter is correct, however position is incorrect
        else:
            color += WHITE_BOX  # Incorrect letter and position
        index += 1
    return color


def input_guess(word_length: int) -> str:
    """Prompts the user to guess until they guess the expected length."""
    word_entry: str = input(f"Enter a {word_length} character word: ")
    while len(word_entry) != word_length:
        word_entry = input(f"That wasn't {word_length} chars! Try again: ")
    print(word_entry)
    return word_entry


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    num_turn: int = 1
    max_turns: int = 6
    win = False

    while num_turn <= max_turns and not win:
        print(f"=== Turn {num_turn}/{max_turns} ===")
        guess = input_guess(len(secret))
        final_result = emojified(guess, secret)
        print(final_result)
        if guess == secret:
            win = True
        else:
            num_turn += 1
    # print for results of game
    if win:
        print(f"You won in {num_turn}/{max_turns} turns!")
    else:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
