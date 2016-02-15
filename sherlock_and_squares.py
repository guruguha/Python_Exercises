import math

t = int(input().strip())
for a0 in range(t):
    n = input().strip()
    lo,hi = n.split(' ')
    a = math.ceil(math.sqrt(int(lo)))
    b = math.floor(math.sqrt(int(hi)))
    print(int(b - a) + 1)
