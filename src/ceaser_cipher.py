# -*- coding: utf-8 -*-
# in this first lab we are going to create a encryption/decryption program


def encrypt(message, key=3):
    """return the cipher Message based on the given Message and Key"""
    # here the message in an uppercase
    # write your code here
    encrypted = ""
    for caracter  in message:
        if ord(caracter)<128:
            caracter_trans = chr((ord(caracter) + (key % 128))%128)
        else:
            caracter_trans = caracter
        encrypted += caracter_trans
    return encrypted

def decrypt(cipher, key=3):
    """return the Plain Message based on the given Cipher_Message and Key"""
    # here the cipher in an uppercase
    # write your code here
    encrypted = ""
    for caracter  in cipher:
        if ord(caracter)<=128:
            caracter_trans = chr((ord(caracter) - (key % 128))%128)
        else:
            caracter_trans = caracter
        encrypted += caracter_trans
    return encrypted


M = "bonjour123456!%!£$!Q%432"
M2 = "abcd$%"
M3 = "EFGHIZ12341$%"

#print(encrypt(M))
#print(encrypt(M2))
#print(encrypt(M3))
print(decrypt(encrypt(M)))
print(decrypt(encrypt(M2)))
print(decrypt(encrypt(M3)))