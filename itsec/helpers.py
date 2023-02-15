"""
contains helper functions
"""


def calculate_inverse_multiplicative(t: int) -> int:
    """Calculate the inverse multiplicative of a number."""
    for i in range(1, 26):
        if (t * i) % 26 == 1:
            return i
    raise ValueError(f"No inverse multiplicative for '{t}' found.")


def print_matrix(matrix: list[list[str]]) -> None:
    """Print a matrix."""
    for row in matrix:
        for char in row:
            print(char, end=" ")
        print()
