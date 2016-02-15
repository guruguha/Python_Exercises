#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
rev = [str(x) for x in reversed(arr)]
print(' '.join(rev))
