from typing import Tuple

def encrypt_one_time_pad_chiffre(plain_text: str, k: str) -> list[int]:
    """
    Encrypts a string using the one-time pad chiffre.
    """
    plain = [ord(c) for c in plain_text]
    key = [ord(c) for c in k]
    res = []
    for i, c in enumerate(plain):
        res.append(c ^ key[i])

    return res

def decrypt_one_time_pad_chiffre(cipher: list[int], k: str) -> str:
    """
    Decrypts a string using the one-time pad chiffre.
    """
    return ""
