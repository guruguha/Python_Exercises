#!/bin/python3
import re
import sys


def match_sub_array(ptn, grid, begin, end):
    j = 0
    for i in range(len(grid)):
        if j < len(ptn):
            if ''.join(ptn[j]) not in ''.join(grid[i][begin:end]):
                return False
            else:
                j += 1
        else:
            break

    if j == len(ptn):
        return True
    else:
        return False


def match(begin):
    end = len(pat_line1_str) + begin
    # x,y = find_pattern(pat_line1_str, ''.join(G[i]))
    if match_sub_array(P[1:],G[i+1:], begin, end):
        return True
    else:
        return False


t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
        G_t = str(input().strip())
        G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
        P_t = str(input().strip())
        P.append(P_t)

    pat_line1 = P[0]
    pat_line1_str = ''.join(pat_line1)

    for i in range(len(G)):
        pat_occurence = [m.start() for m in re.finditer(pat_line1_str, G[i])]
        if len(pat_occurence) > 1:
            done = False
            for i in range(len(pat_occurence)):
                if match(pat_occurence[i]):
                    print("YES")
                    done = True
                    break
                else:
                    continue

            if not done:
                print("NO")
        else:
            begin = ''.join(G[i]).find(pat_line1_str)
            if match(begin):
                print("YES")
            else:
                print("NO")

