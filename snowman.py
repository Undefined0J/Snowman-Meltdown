"""Main entry point for Snowman Meltdown."""
from game_logic import play_game


def main() -> None:
    """Start the application and handle replay functionality."""
    while True:
        play_game()

        replay = input("Do you want to play again? (y/n): ").lower().strip()
        if replay != "y":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()