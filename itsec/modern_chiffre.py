from typing import Tuple
from .helpers import *
from .constants import *

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

    right_part_sbox_0 = apply_simplified_des_sbox(right_part_expanded_xor_k[:4], DES_S0)
    right_part_sbox_1 = apply_simplified_des_sbox(right_part_expanded_xor_k[4:], DES_S1)
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
