from itsec.classic_chiffre import *

key = 7
t = 5

caesar_encrypted = encrypt_caesar_chiffre("test", key)
caesar_decrypted = decrypt_caesar_chiffre(caesar_encrypted[0], key)

print("encrypted: ", caesar_encrypted)
print("decrypted: ", caesar_decrypted)

affine_encrypted = encrypt_affine_chiffre("test", t, key)
affine_decrypted = decrypt_affine_chiffre(affine_encrypted[0], t, key)

print("encrypted: ", affine_encrypted)
print("decrypted: ", affine_decrypted)

