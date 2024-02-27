import string


def key_matrix_generation(key):
    atoz = string.ascii_lowercase.replace('j', '.')

    key_matrix = ['' for i in range(5)]

    i = 0
    j = 0

    for c in key:
        if c in atoz:
            key_matrix[i] += c
            atoz = atoz.replace(c, '.')

            j += 1
            if j > 4:
                i += 1
                j = 0

    for c in atoz:
        if c != '.':
            key_matrix[i] += c

            j += 1
            if j > 4:
                i += 1
                j = 0

    return key_matrix


key_matrix = key_matrix_generation('playfire example')


def encryption(plaintext, key_matrix):
    plaintextpair = []
    ciphertextpairs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        b = ''

        if i + 1 == len(plaintext):
            b += 'x'
        else:
            b = plaintext[i + 1]

        if a != b:
            plaintextpair.append(a + b)
            i += 2
        else:
            plaintextpair.append(a + 'x')
            i += 1

    # rule 2

    for pair in plaintextpair:
        applied_rule = False
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])

                ciphertextpair = row[(j0 + 1) % 5] + row[(j1 + 1) % 5]
                ciphertextpairs.append(ciphertextpair)
                applied_rule = True

        if applied_rule:
            continue

        for j in range(5):
            col = "".join(key_matrix[i][j] for i in range(5))
            if pair[0] in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])

                ciphertextpair = col[(i0 + 1) % 5] + col[(i1 + 1) % 5]
                ciphertextpairs.append(ciphertextpair)
                applied_rule = True

        if applied_rule:
            continue

        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0

        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])

            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])

        ciphertextpair = key_matrix[i0][j1] + key_matrix[i1][j0]
        ciphertextpairs.append(ciphertextpair)

    return "".join(ciphertextpairs)


def decryption(text, key_matrix):
    plaintextpairs = []
    ciphertextpairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1]

        ciphertextpairs.append(a + b)
        i += 2

    # rule 2

    for pair in ciphertextpairs:
        applied_rule = False
        for row in key_matrix:
            if pair[0] in row and pair[1] in row:
                j0 = row.find(pair[0])
                j1 = row.find(pair[1])

                plaintext = row[(j0 + 4) % 5] + row[(j1 + 4) % 5]
                plaintextpairs.append(plaintext)
                applied_rule = True

        if applied_rule:
            continue

        for j in range(5):
            col = "".join(key_matrix[i][j] for i in range(5))
            if pair[0] in col and pair[1] in col:
                i0 = col.find(pair[0])
                i1 = col.find(pair[1])

                plaintext = col[(i0 + 4) % 5] + col[(i1 + 4) % 5]
                plaintextpairs.append(plaintext)
                applied_rule = True

        if applied_rule:
            continue

        i0 = 0
        i1 = 0
        j0 = 0
        j1 = 0

        for i in range(5):
            row = key_matrix[i]
            if pair[0] in row:
                i0 = i
                j0 = row.find(pair[0])

            if pair[1] in row:
                i1 = i
                j1 = row.find(pair[1])

        plaintext = key_matrix[i0][j1] + key_matrix[i1][j0]
        plaintextpairs.append(plaintext)

    return "".join(plaintextpairs)


print('Key :playfire example')
plaintext = 'hide the gold in the tree stump'
plaintext = plaintext.replace(' ', '')
encryption = encryption(plaintext, key_matrix)
print("Decryption :" + encryption)
encrypt = decryption(encryption, key_matrix)
print('Encryption :' + encrypt)
