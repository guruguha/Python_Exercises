#!/bin/python3

import math


t = int(input().strip())

for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    total = 0
    wraps = num_chocs = int(n/c)

    while wraps >= m:
        newlyEaten = wraps/m
        num_chocs += newlyEaten
        wraps %= m
        wraps += newlyEaten

    print(int(num_chocs))
