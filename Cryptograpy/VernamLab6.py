import string
import random
import numpy as np

alphabet = string.ascii_lowercase

mp = dict(zip(alphabet, range(len(alphabet))))
mp2 = dict(zip(range(len(alphabet)), alphabet))


def generateKey(length):
    key = ''
    for i in range(length):
        key += chr(random.randint(65, 90))
    return key


def encrypt(message, key):
    encrypted_message = ''
    encrypted_code = []
    for i in range(len(message)):
        xor = mp[message[i]] ^ mp[key[i]]
        encrypted_code.append(xor)
        encrypted_message += mp2[xor % 26]
    return encrypted_message, encrypted_code

def decrypt(encrypted_code, key):
    decryption_message = ''
    for i in range(len(encrypted_code)):
        xor = encrypted_code[i] ^ mp[key[i]]
        decryption_message += mp2[xor % 26]
    return decryption_message


# Input section
message = 'oak'
key = generateKey(len(message)).lower()
encrypted_message, encrypted_code= encrypt(message, key)
decryption_message = decrypt(encrypted_code, key)
print("Encryption Message : "+encrypted_message)
print('Decrypted Message : '+decryption_message)
