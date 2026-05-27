"""Main entry point for Snowman Meltdown."""
from data import WORDS
from game_logic import get_random_word


def play_game() -> None:
    """Run the main game loop."""
    secret_word = get_random_word(WORDS)

    print("Welcome to Snowman Meltdown!")
    print(f"Secret word selected: {secret_word}")  # For testing, remove later

    # Initial user prompt
    guess = input("Guess a letter: ").lower()
    print(f"You guessed: {guess}")


if __name__ == "__main__":
    play_game()