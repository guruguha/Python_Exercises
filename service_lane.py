#!/bin/python3

import sys


n,t = input().strip().split(' ')
n,t = [int(n),int(t)]
width = [int(width_temp) for width_temp in input().strip().split(' ')]
for a0 in range(t):
    i,j = input().strip().split(' ')
    i,j = [int(i),int(j)]

    segment_width = width[i:j+1]

    segment_width.sort()
    if segment_width[0] >= 3:
        print(3)
    elif segment_width[0] >= 2:
        print(2)
    elif segment_width[0] >= 1:
        print(1)
