"""Main entry point for Snowman Meltdown."""
from data import WORDS
from game_logic import get_random_word, display_game_state


def play_game() -> None:
    """Run the main game loop."""
    secret_word = get_random_word(WORDS)
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")

    # Display the initial game state
    display_game_state(mistakes, secret_word, guessed_letters)

    # Prompt user for one guess
    guess = input("Guess a letter: ").lower()
    print(f"You guessed: {guess}")


if __name__ == "__main__":
    play_game()