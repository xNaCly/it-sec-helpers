"""
This module contains the implementations of several modern cryptographic algorithms.

- one-time pad chiffre
- simplified DES
- RSA
"""
from typing import Tuple
from .helpers import *
from .constants import *
from math import gcd


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


def create_simplified_des_subkeys(key: str) -> Tuple[str, str]:
    """
    Creates the two keys for simplified DES (k1, k2).
    key is the binary representation of the encryption key (10 bits).
    """
    assert len(key) == 10

    key = apply_permutation_table(key, DES_P10)
    left_part = key[:5]
    right_part = key[5:]

    left_part_ls1 = left_part[1:] + left_part[0]
    right_part_ls1 = right_part[1:] + right_part[0]

    k1 = apply_permutation_table(left_part_ls1 + right_part_ls1, DES_P8)

    left_part_ls2 = left_part_ls1[2:] + left_part_ls1[:2]
    right_part_ls2 = right_part_ls1[2:] + right_part_ls1[:2]

    k2 = apply_permutation_table(left_part_ls2 + right_part_ls2, DES_P8)

    return k1, k2


def apply_simplified_des_sbox(input: str, sbox: list[list[str]]) -> str:
    """
    Applies a simplified DES S-Box for a 4 bit long cipher part.
    """
    assert len(input) == 4
    row = int(input[0] + input[3], 2)
    col = int(input[1] + input[2], 2)
    return sbox[row][col]


def apply_simplified_des_round(cipher: str, k) -> str:
    """
    Applies a simplified DES row round.
    """

    left_part = cipher[:4]
    right_part = cipher[4:]

    right_part_expanded = apply_permutation_table(right_part, DES_EP)
    right_part_expanded_xor_k = xor_binary_strings(right_part_expanded, k)

    right_part_sbox_0 = apply_simplified_des_sbox(
        right_part_expanded_xor_k[:4], DES_S0)
    right_part_sbox_1 = apply_simplified_des_sbox(
        right_part_expanded_xor_k[4:], DES_S1)
    right_part_sbox = right_part_sbox_0 + right_part_sbox_1

    right_part_p4 = apply_permutation_table(right_part_sbox, DES_P4)

    left_part_xor_p4 = xor_binary_strings(left_part, right_part_p4)

    return left_part_xor_p4 + right_part


def encrypt_simplified_des(plain_binary: str, key: str) -> str:
    """
    Encrypts a binary string using simplified DES.
    plain_binary is the binary representation of the plaintext byte (8 bit).
    key is the binary representation of the encryption key (10 bits).
    """

    assert len(plain_binary) == 8
    k1, k2 = create_simplified_des_subkeys(key)

    cipher = apply_permutation_table(plain_binary, DES_IP)
    cipher = apply_simplified_des_round(cipher, k1)
    cipher = cipher[4:] + cipher[:4]
    cipher = apply_simplified_des_round(cipher, k2)
    cipher = apply_permutation_table(cipher, DES_IP_INV)
    return cipher


def rsa_generate_keys(p: int, q: int) -> list[list[int]]:
    """
    Generates the public and private key for RSA.
    Returns a list of two lists, the first one containing the public key and the second one the private key.
    The public key is a list of two integers, the first one is e of gcd(e, phi) == 1 and the second one the product of p and q.
    """
    n = p * q
    phi = (p-1) * (q-1)
    pe = []
    for i in range(2, phi):
        if gcd(i, phi) == 1:
            pe.append(i)
            if len(pe) == 12:
                break
    e = pe[-1]
    d = 0
    for i in range(0, phi):
        if (i * e) % phi == 1:
            d = i
            break

    return [[e, n], [d, n]]


def encrypt_rsa(public_key: list[int], txt: str) -> list[int]:
    """
    Encrypts a string using RSA.
    """
    def encrypt(c: str) -> int:
        return (ord(c) ** public_key[0]) % public_key[1]
    return [encrypt(c) for c in txt]


def decrypt_rsa(private_key: list[int], chiffre: list[int]) -> str:
    """
    Decrypts a string using RSA.
    """
    def decrypt(c: int) -> str:
        return chr((c**private_key[0]) % private_key[1])
    return "".join([decrypt(c) for c in chiffre])
