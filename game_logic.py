"""Core game logic for Snowman Meltdown."""
import random
from data import STAGES


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