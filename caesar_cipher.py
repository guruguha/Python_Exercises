#!/bin/python3

import sys


n = int(input().strip())
s = input().strip()
k = int(input().strip())


def encrypt(n, s, k):
    cipher_str = ""
    for char in s:
        if ord(char) < 65 or ord(char) > 90 and ord(char) < 97 or ord(char) > 122:
            cipher_str += char
        else:
            k %= 26
            if (ord(char) + k) > ord('z'):
                req_char = chr((ord(char) + k) - ord('z') + ord('a') - 1)
            elif (ord(char) + k) > ord('Z') and (ord(char) + k) < ord('a'):
                req_char = chr((ord(char) + k) - ord('Z') + ord('A') - 1)
            else:
                req_char = chr(ord(char) + k)
            cipher_str += req_char


    return cipher_str


cipher = encrypt(n,s,k)
print(cipher)
