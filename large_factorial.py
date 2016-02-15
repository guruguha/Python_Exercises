#!/bin/python3

import sys


n = int(input().strip())

fact = 1
itr = 1
while itr <= n:
    fact *= itr
    itr += 1

print(fact)
