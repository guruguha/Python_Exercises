__author__ = 'Guruguha'

str = input()

def palindrome(str):
    table = [[0 for x in range(len(str))] for x in range(len(str))]
    palin_set = set()

    if len(str) == 0:
        return 0

    if len(str) == 1:
        return 1

    if len(str) == 2:
        return 2

    for i in range(0, len(str)):
        table[i][i] = 1
        palin_set.add(str[i])

    for i in range(0, len(str) - 1):
        if str[i+1] == str[i]:
            palin_set.add(str[i:i+2])
            table[i][i] = 1

    for length in range(3, (len(str))+1):
        i = 0
        while i < (len(str) - length + 1):
            j = i + length - 1
            if table[i+1][j-1] == 1 and str[i] == str[j]:
                palin_set.add(str[i:i+length])
                table[i][j] = 1
            i += 1
    print(palin_set)
    return len(palin_set)
if len(str) < 5000:
    cnt = palindrome(str)
    print(cnt)

