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

def apply_permutation_table(input: str, table: str) -> str:
    """Applies a permutation table to a input string."""
    output = ""
    for i in table:
        output += input[int(i) - 1]
    return output

def xor_binary_strings(a: str, b: str) -> str:
    """XOR two binary strings."""
    assert len(a) == len(b)
    return "".join([str(int(a[i]) ^ int(b[i])) for i in range(len(a))])
