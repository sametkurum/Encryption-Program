# ENCRYTION PROGRAM

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

#encrption
plain_text = input("What will you encrypt?: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

#decryption
encrypted_text = input("What is the encrytion text?: ")
decrypted_text = ""

for letter in encrypted_text:
    index = key.index(letter)
    decrypted_text += chars[index]

print(f"Encrypted message: {encrypted_text}")
print(f"Original message: {decrypted_text}")