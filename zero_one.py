__author__ = 'Guruguha'

# Find if any multiple has only zeros and ones

num = int(input())
if num in range(0, 100000):
    for i in range(1, 2**num):
        bin_num = int(bin(i)[2:])
        if not bin_num % num:
            print(bin_num)
            break
