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


def decrypt_one_time_pad_chiffre(cipher: list[int], k: str) -> Tuple[str, list[int]]:
    """
    Decrypts a string using the one-time pad chiffre.
    """
    key = [ord(c) for c in k]
    res = []
    for i, c in enumerate(cipher):
        res.append(c ^ key[i])
    return ("".join([chr(x) for x in res]), res)
