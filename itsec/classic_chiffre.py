"""
This module contains the implementations of several classic cryptographic algorithms.

- caesar chiffre
- multiplicative chiffre
- affine chiffre
- playfair chiffre
"""
from typing import Tuple

from .constants import ALPHABET
from .helpers import calculate_inverse_multiplicative, print_matrix


def encrypt_caesar_chiffre(plain_text: str, k: int) -> Tuple[str, list[int]]:
    """Encrypt a plain text with the caesar chiffre.

    ! fails if plain_text contains characters not in ALPHABET

    Args:
        plain_text (str): The plain text to encrypt.
        k (int): The key
    """
    plain_text = plain_text.lower().replace(" ", "")
    ints = [ALPHABET.index(char) for char in plain_text]
    ints = [(i + k) % 26 for i in ints]
    return ("".join([ALPHABET[i] for i in ints]), ints)


def decrypt_caesar_chiffre(cipher_text: str, k: int) -> Tuple[str, list[int]]:
    """Decrypt a cipher text with the caesar chiffre.

    ! fails if cipher_text contains characters not in ALPHABET

    Args:
        cipher_text (str): The cipher text to encrypt.
        k (int): The key
    """
    cipher_text = cipher_text.lower().replace(" ", "")
    ints = [ALPHABET.index(char) for char in cipher_text]
    ints = [(i - k) % 26 for i in ints]
    return ("".join([ALPHABET[i] for i in ints]), ints)


def encrypt_multiplicative_chiffre(plain_text: str, t: int) -> Tuple[str, list[int]]:
    """Encrypt a plain text with the multiplicative chiffre.

    ! fails if plain_text contains characters not in ALPHABET

    Args:
        plain_text (str): The plain text to encrypt.
        k (int): The key
    """
    plain_text = plain_text.lower().replace(" ", "")
    ints = [ALPHABET.index(char) for char in plain_text]
    ints = [(i * t) % 26 for i in ints]
    return ("".join([ALPHABET[i] for i in ints]), ints)


def decrypt_multiplicative_chiffre(cipher_text: str, t: int) -> Tuple[str, list[int]]:
    """Decrypt a cipher text with the multiplicative chiffre.

    ! fails if cipher_text contains characters not in ALPHABET

    Args:
        cipher_text (str): The cipher text to decrypt.
        k (int): The key
    """
    inv = calculate_inverse_multiplicative(t)
    cipher_text = cipher_text.lower().replace(" ", "")
    ints = [ALPHABET.index(char) for char in cipher_text]
    ints = [(i * inv) % 26 for i in ints]
    return ("".join([ALPHABET[i] for i in ints]), ints)


def encrypt_affine_chiffre(plain_text: str, t: int, k: int) -> Tuple[str, list[int]]:
    """Encrypt a plain text with the affine chiffre.

    ! fails if cipher_text contains characters not in ALPHABET

    Args:
        plain_text (str): The plain text to encrypt.
        t (int): The multiplicate value.
        k (int): The key
    """
    plain_text = plain_text.lower().replace(" ", "")
    ints = [ALPHABET.index(char) for char in plain_text]
    ints = [(i * t + k) % 26 for i in ints]
    return ("".join([ALPHABET[i] for i in ints]), ints)


def decrypt_affine_chiffre(cipher_text: str, t: int, k: int) -> Tuple[str, list[int]]:
    """Decrypt a cipher text with the affine chiffre.

    ! fails if cipher_text is not encoded with the affine chiffre
    ! fails if cipher_text contains characters not in ALPHABET

    Args:
        cipher_text (str): The cipher text to decrypt.
        t (int): The multiplicate value.
        k (int): The key
    """
    cipher_text = cipher_text.lower().replace(" ", "")
    inv = calculate_inverse_multiplicative(t)
    ints = [ALPHABET.index(char) for char in cipher_text]
    ints = [(i - k) * inv % 26 for i in ints]
    return ("".join([ALPHABET[i] for i in ints]), ints)


# TODO: implement playfair chiffre
def encrypt_playfair_chiffre(plain_text: str, k: str) -> Tuple[str, list[int]]:
    """Encrypt a plain text with the playfair chiffre.

    ! fails if plain_text contains characters not in ALPHABET

    Args:
        plain_text (str): The plain text to encrypt.
        k (str): The key
    """
    plain_text = plain_text.replace(" ", "x")
    formated_text = ""
    lc = ""

    for c in plain_text:
        if lc == c:
            formated_text += "x"
        formated_text += c
        lc = c

    pairs = [formated_text[i: i + 2] for i in range(0, len(formated_text), 2)]

    for i, c in enumerate(pairs):
        if len(c) == 1:
            pairs[i] += "x"

    key = ""
    for c in k:
        if c not in key:
            key += c

    matrix = []
    alphabet = key + \
        "".join(sorted(list(set(ALPHABET.replace("j", "")) - set(k))))

    pos_map = {}

    for i in range(5):
        col = []
        for j in range(5):
            pos = i * 5 + j
            char = alphabet[pos]
            pos_map[char] = (i, j)
            col.append(char)
        matrix.append(col)

    print("Matrix: ")
    print_matrix(matrix)

    for i in pairs:
        y1, x1 = pos_map[i[0]]
        y2, x2 = pos_map[i[1]]
        if y1 == y2:
            print("Same row")
        elif x1 == x2:
            print("Same col")
        else:
            print("gotta make a cube")

    return ("", [])


def encrypt_polybios_chiffre(plain_text: str, k: str) -> Tuple[str, list[int]]:
    """Encrypt a plain text with the polybios chiffre.

    ! fails if plain_text contains characters not in ALPHABET

    ! i and j are replacable, i choose to use i everywhere, if your encrypted text includes j it will be replaced to i

    Args:
        plain_text (str): The plain text to encrypt.
        k (str): The key
    """
    plain_text = plain_text.lower().replace(" ", "")
    key = ""
    for c in k:
        if c not in key:
            key += c

    matrix = []
    alphabet = key + \
        "".join(sorted(list(set(ALPHABET.replace("j", "")) - set(k))))

    pos_map = {}

    for x in range(5):
        col = []
        for y in range(5):
            pos = x * 5 + y
            char = alphabet[pos]
            if char == 'i':
                pos_map['j'] = (x+1, y+1)
            pos_map[char] = (x+1, y+1)
            col.append(char)
        matrix.append(col)

    print_matrix(matrix)

    ints = [pos_map[c] for c in plain_text]
    return ("".join([str(i[1]) + str(i[0]) for i in ints]), ints)


def decrypt_polybios_chiffre(chiffre_text: str, k: str) -> Tuple[str, list[int]]:
    """Decrpyt a chiffre text with the polybios chiffre.

    ! fails if chiffre isnt made up of integers

    ! i and j are replacable, i choose to use i everywhere, if your encrypted text includes j it will be replaced to i

    Args:
        chiffre_text (str): The plain text to encrypt.
        k (str): The key
    """
    key = ""
    for c in k:
        if c not in key:
            key += c

    matrix = []
    alphabet = key + \
        "".join(sorted(list(set(ALPHABET.replace("j", "")) - set(k))))

    for x in range(5):
        col = []
        for y in range(5):
            col.append(alphabet[x * 5 + y])
        matrix.append(col)

    pairs = [chiffre_text[i: i + 2] for i in range(0, len(chiffre_text), 2)]
    ints = []

    for i in pairs:
        ints.append((int(i[0]), int(i[1])))

    chars = [matrix[i[1]-1][i[0]-1] for i in ints]

    return ("".join(chars), ints)
