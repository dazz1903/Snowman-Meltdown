import random

from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Select and return a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage and the currently revealed letters."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print()


def play_game():
    """Play until the word is guessed or the snowman melts."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    while mistakes < MAX_MISTAKES and not all(
        letter in guessed_letters for letter in secret_word
    ):
        display_game_state(mistakes, secret_word, guessed_letters)
        guess = input("Guess a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try another letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            mistakes += 1
            print("Incorrect guess. Mistakes:", mistakes)

    display_game_state(mistakes, secret_word, guessed_letters)

    if all(letter in guessed_letters for letter in secret_word):
        print("You saved the snowman!")
    else:
        print("The snowman melted! The word was:", secret_word)
