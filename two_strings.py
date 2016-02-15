n = int(input().strip())

for i in range(0, n):
    str1 = str(input())
    str2 = str(input())

    set1 = set(str1)
    set2 = set(str2)

    if set.intersection(set1, set2):
        print("YES")
    else:
        print("NO")
        
