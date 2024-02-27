def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key
    else:
        key = key

    for letter in text:
        letter = letter.lower()
        if not letter == ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result


# input section
letters = 'abcdefghijklmnopqrstuvwxyz'
plaintext = input('Enter your text : ')
mode = input("e/d: ")
num_letters = len(letters)
key = int(input('Enter key through 1 to 26 : '))
value = encrypt_decrypt(plaintext, mode, key)
print(value)
