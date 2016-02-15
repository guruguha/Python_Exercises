import sys

import math

import itertools

s = input().strip()
join_text = ''.join(s.split())
rows, cols = math.floor(math.sqrt(len(join_text))), math.ceil(math.sqrt(len(join_text)))
grid = []
length = len(s)
i = 0

# dim = int(len(join_text)**0.5)
# if dim * dim == len(s):
#     x, y = dim, dim
# else:
#     x, y = dim, dim + 1
# #
# # array = [join_text[i : i + y] for i in range(0, len(s), y)]
# # transpose = itertools.zip_longest(*array, fillvalue = '')
# # print(' '.join(''.join(s) for s in transpose))

while i < cols:
    sub_grid = ""
    j = i
    while j < length:
        sub_grid += join_text[j]
        j += rows + 1
    i += 1
    grid.append(sub_grid)

print(' '.join(grid))
#
#     sub_grid = list(join_text[from_idx:to_idx])
#     # sub_grid_list = list(sub_grid)
#     grid.append(sub_grid)
#     remaining -= len(sub_grid)
#
#     if remaining == 0:
#         not_done = False
#     elif remaining < rows:
#         from_idx = to_idx
#         to_idx += remaining
#     else:
#         from_idx = to_idx
#         to_idx += rows + 1
#
# final_list = list(zip(*grid))
# for sub_list in final_list:
#     print(''.join(sub_list) + " ")
