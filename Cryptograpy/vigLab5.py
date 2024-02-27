def Vigenere(text, s, Flag):
    result = ''
    for i in range(len(text)):
        char = text[i]
        if(Flag):
            result += chr((ord(char) - 97 + ord(s[i]) - 97) % 26 + 97)
        else:
            result += chr((ord(char) - ord(s[i]) + 26) % 26 + 97)
    return result


key = "".join(input('Enter the key : ').lower().split())
plain = ''.join(input('Enter PlainText: ').lower().split())
s = ''
catpillar = 0
for i in range(len(plain)):
    s += key[catpillar % len(key)]
    catpillar += 1

Encrypt = Vigenere(plain, s, True)
print('Encryption Message : '+Encrypt)
Decrypt = Vigenere(Encrypt, s, False)
print('Decryption Message :' + Decrypt)
