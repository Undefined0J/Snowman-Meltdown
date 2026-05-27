"""Core game logic for Snowman Meltdown."""
import random
import os
from ascii_art import STAGES
from data import WORDS


def clear_console() -> None:
    """Clear the terminal screen for a cleaner UI."""
    os.system("cls" if os.name == "nt" else "clear")


def get_random_word(word_list: list) -> str:
    """Select and return a random word from the provided list."""
    return random.choice(word_list)


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list) -> None:
    """Display the snowman stage and the currently revealed word."""
    clear_console()
    print("Welcome to Snowman Meltdown!\n")
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += f"{letter} "
        else:
            display_word += "_ "

    print(f"Word:  {display_word.strip()}\n")


def is_word_guessed(secret_word: str, guessed_letters: list) -> bool:
    """Check if all letters in the secret word have been successfully guessed."""
    for letter in secret_word:
        if letter not in guessed_letters:
            return False
    return True


def get_valid_guess(guessed_letters: list) -> str:
    """Prompt the user until a valid, single, un-guessed alphabetical letter is provided."""
    while True:
        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter exactly one alphabetical letter.")
        elif guess in guessed_letters:
            print("You already guessed that letter. Try a different one.")
        else:
            return guess


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

        guess = get_valid_guess(guessed_letters)
        guessed_letters.append(guess)

        # Process the guess
        if guess not in secret_word:
            mistakes += 1

        # Check for win condition
        if is_word_guessed(secret_word, guessed_letters):
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations, you saved the snowman!")
            return

    # Check for loss condition (loop ended because max_mistakes was reached)
    display_game_state(mistakes, secret_word, guessed_letters)
    print(f"Game Over! The word was: {secret_word}")
