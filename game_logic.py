"""Core game logic for Snowman Meltdown."""
import random


def get_random_word(word_list: list) -> str:
    """Select and return a random word from the provided list."""
    return random.choice(word_list)