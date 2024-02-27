import math
import numpy as np
import sympy


# Generating Key Matrix
def KeyMatrix(key, n):
    Matrix = []
    for i in range(n):
        temp = list()
        for j in range(n):
            temp.append(ord(key[i * n + j]) - 97)
        Matrix.append(temp)
    if np.linalg.det(Matrix) == 0:
        print('Invalid Key!')
        exit(None)
    return Matrix


def Multiply(X, Y):
    Y = list([ord(x) - 97 for x in Y])
    result = np.zeros([len(Y), 1], dtype=int)
    result = np.dot(X, Y)
    return result


def modInverse(a, m):
    a = a % m
    for x in range(1, m):
        if ((a * x) % m == 1):
            return x
    return 1


# Generate Inverse Key matrix

def InverserKeyMatrix(key, n):
    Matrix = []
    for i in range(n):
        temp = list()
        for j in range(n):
            temp.append(ord(key[i * n + j]) - 97)
        Matrix.append(temp)
    d = math.floor(np.linalg.det(Matrix))
    if d == 0:
        print('Invalid key')
        exit(None)
    A = sympy.Matrix(Matrix)
    A = (A.adjugate() * modInverse(d, 26)) % 26

    for i in range(n):
        for j in range(n):
            Matrix[i][j] = A[i, j]
    return Matrix


# Encryption section
def Hill_encrypt(plain, Matrix, n):
    cipher = ""
    for i in range(0, len(plain), n):
        temp = Multiply(Matrix, plain[i:i + n])
        for x in range(n):
            cipher += chr(temp[x] % 26 + 97)
    return cipher


# input section
def main():
    key = ''.join(input('Enter key : ').lower().split())
    plain = ''.join(input('Enter text :').lower().split())
    n = math.sqrt(len(key))

    if n != math.trunc(n) or n == 0:
        print('Invalid Key!')
        exit(None)
    n = math.floor(n)
    if len(plain) % n != 0:
        for i in range(n - len(plain) % n):
            plain += 'x'
    Matrix = KeyMatrix(key, n)
    InverseMatrix = InverserKeyMatrix(key, n)
    cipherText = Hill_encrypt(plain, Matrix, n)
    print('CipherText ' + cipherText)
    # print('Inverse Key : ', InverseMatrix)
    print('PlainText : ' + Hill_encrypt(cipherText, InverseMatrix, n))


main()

# Enter key : cddg
# Enter text :attack
# CipherText fkmfio
