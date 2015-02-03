__author__ = 'Guruguha'

# Lambda and map functions

num = int(input())
fib_list = []
fib_list.append(str(0))
fib_list.append(str(1))
if num == 0:
    empty = []
    print(empty)
elif num == 1:
    one_list = [0]
    print(one_list)
else:
    cnt = 1
    while cnt != num - 1:
        fib_list.append(str(int(fib_list[cnt]) + int(fib_list[cnt - 1])))
        cnt += 1
    cube = lambda a: int(a) * int(a) * int(a)

    print(list(map(cube, fib_list)))

