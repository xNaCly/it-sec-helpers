"""
This module contains the classic chiffre algorithms.
- caesar chiffre
- affine chiffre
"""
from typing import Tuple

from .constants import ALPHABET
from .helpers import calculate_inverse_multiplicative

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

