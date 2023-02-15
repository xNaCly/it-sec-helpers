from itsec.classic_chiffre import *

key = 7
t = 5

# print(encrypt_playfair_chiffre("vaccine is based on messenger rna", "curevac"))
print("\nPolybios Chiffre")
polybios_encrypted = encrypt_polybios_chiffre("kryptographie", "dhbw")
polybios_decrypted = decrypt_polybios_chiffre(polybios_encrypted[0], "dhbw")

print("encrypted: ", polybios_encrypted)
print("decrypted: ", polybios_decrypted)


print("\nCaesar Chiffre")
caesar_encrypted = encrypt_caesar_chiffre("test", key)
caesar_decrypted = decrypt_caesar_chiffre(caesar_encrypted[0], key)

print("encrypted: ", caesar_encrypted)
print("decrypted: ", caesar_decrypted)

print("\nMultiplicative Chiffre")

mul_encrypted = encrypt_multiplicative_chiffre("test", t)
mul_decrypted = decrypt_multiplicative_chiffre(mul_encrypted[0], t)

print("encrypted: ", mul_encrypted)
print("decrypted: ", mul_decrypted)

print("\nAffine Chiffre")

affine_encrypted = encrypt_affine_chiffre("test", t, key)
affine_decrypted = decrypt_affine_chiffre(affine_encrypted[0], t, key)

print("encrypted: ", affine_encrypted)
print("decrypted: ", affine_decrypted)
