from enum import Enum

PADDING: int = 20


class Color(Enum):
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    YELLOW = "\033[33m"
    WHITE = "\033[37m"
    REVERSE = "\033[;7m"
    RESET = "\033[0m"


def change_color(color: Color) -> None:
    print(color.value, end="")

# Example usage:
# change_color(Color.RED)
# print("This text will be red.")
# change_color(Color.RESET)
     