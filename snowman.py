import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII art stages
STAGES = [
    # Stage 0: Full snowman
    r"""
     ___
    /___\
    (o o)
    ( : )
    ( : )
    """,
    # Stage 1: Bottom part starts melting
    r"""
     ___
    /___\
    (o o)
    ( : )
    """,
    # Stage 2: Only the head remains
    r"""
     ___
    /___\
    (o o)
    """,
    # Stage 3: Snowman completely melted
    r"""
     ___
    /___\
    """
]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Display the snowman stage and the currently revealed letters."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word: ", display_word)
    print()


def play_game():
    """Start the game and prompt for one letter guess."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    # Guessing logic will be added in a later step.
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


if __name__ == "__main__":
    play_game()
