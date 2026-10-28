import random

from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]
MAX_MISTAKES = len(STAGES) - 1


def get_random_word():
    """Select and return a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman, word progress, and guesses so far."""
    print("\n" + STAGES[mistakes].strip("\n"))
    print(f"Mistakes remaining: {MAX_MISTAKES - mistakes}")

    display_word = " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )
    print(f"Word: {display_word}")

    if guessed_letters:
        print("Guessed letters: " + ", ".join(guessed_letters))
    else:
        print("Guessed letters: none")


def play_game():
    """Play rounds until the user chooses not to replay."""
    print("Welcome to Snowman Meltdown!")

    while True:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0

        while mistakes < MAX_MISTAKES and not all(
            letter in guessed_letters for letter in secret_word
        ):
            display_game_state(mistakes, secret_word, guessed_letters)
            guess = input("Guess a letter: ").strip().lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter one alphabetical letter.")
                continue

            if guess in guessed_letters:
                print(f"You already guessed '{guess}'. Try another letter.")
                continue

            guessed_letters.append(guess)

            if guess in secret_word:
                print("Correct guess!")
            else:
                mistakes += 1
                print("Incorrect guess.")

        display_game_state(mistakes, secret_word, guessed_letters)

        if all(letter in guessed_letters for letter in secret_word):
            print("You saved the snowman!")
        else:
            print("The snowman melted! The word was:", secret_word)

        while True:
            replay = input("Play again? (y/n): ").strip().lower()

            if replay in ("y", "n"):
                break

            print("Please enter y or n.")

        if replay == "n":
            print("Thanks for playing!")
            break
