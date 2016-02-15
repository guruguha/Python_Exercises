#!/bin/python3

n = int(input().strip())
num = [int(arr_temp) for arr_temp in input().strip().split(' ')]
num.sort()
# l = len(arr)
# tmp = []
# for i in range(l):
#     if arr[i] < 0:
#         continue
#     else:
#         tmp.append(l - i)
#         cut_length = arr[i]
#         for j in range(i, l):
#             arr[j] -= cut_length
#
# for i in tmp:
#     print(i)



# while l > 0:
#     while l > 0 >= arr[l-1]:
#         arr.pop(l-1)
#         l = len(arr)
#     if l != 0:
#         print(l)
#         arr = [(x-cut_length) for x in arr]


length = len(num)
n = []
num.sort()
for i in range(length):
    if num[i] <= 0:
        continue
    else:
        n.append(length - i)
        v = num[i]
        for j in range(i, length):
            num[j] -= v
    # print(num)
print("\n".join(map(str, n)))
