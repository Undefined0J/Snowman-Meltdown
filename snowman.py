"""Main entry point for Snowman Meltdown."""
from game_logic import play_game


def main() -> None:
    """Start the application and handle replay functionality."""
    while True:
        play_game()

        while True:
            replay = input("Do you want to play again? (y/n): ").lower().strip()
            if replay in ("y", "n"):
                break
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

        if replay == "n":
            print("Thanks for playing! Goodbye.")
            break


if __name__ == "__main__":
    main()