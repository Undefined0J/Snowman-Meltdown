"""Core game logic for Snowman Meltdown."""
import random
from ascii_art import STAGES
from data import WORDS


def get_random_word(word_list: list) -> str:
    """Select and return a random word from the provided list."""
    return random.choice(word_list)


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list) -> None:
    """Display the snowman stage and the currently revealed word."""
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += f"{letter} "
        else:
            display_word += "_ "

    print(f"Word: {display_word.strip()}\n")


def is_word_guessed(secret_word: str, guessed_letters: list) -> bool:
    """Check if all letters in the secret word have been successfully guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def play_game() -> None:
    """Run the main game loop."""
    secret_word = get_random_word(WORDS)
    guessed_letters = []
    mistakes = 0
    max_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    # Main game loop
    while mistakes < max_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        # Process the guess
        if guess not in guessed_letters:
            guessed_letters.append(guess)
            if guess not in secret_word:
                mistakes += 1

        # Check for win condition
        if is_word_guessed(secret_word, guessed_letters):
            print("Congratulations, you saved the snowman!")
            return

    # Check for loss condition (loop ended because max_mistakes was reached)
    print(f"Game Over! The word was: {secret_word}")
    print(STAGES[mistakes])