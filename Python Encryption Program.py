import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

#print(f"chars: {chars}")
#print(f"key: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    #finds where the character is located in the list
    cipher_text += key[index]
    #uses that location to take a shuffled character

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

#DECRYPT
cipher_text = input("Enter a message to encrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    #finds where the character is located in the list
    plain_text += chars[index]
    #uses that location to take a shuffled character

print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
