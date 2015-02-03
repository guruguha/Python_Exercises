__author__ = 'Guruguha'

# Find substring count
main_string = input()
sub_string = input()
sub_str_cnt = 0


def find_sub_string(j, main_str, sub_str):
    cnt = 0
    for k in range(0, len(sub_str)):
        if main_str[j + k] != sub_str[k]:
            break
        else:
            cnt += 1
    if cnt == len(sub_string):
        return True
    else:
        return False

if len(main_string) > 200 or len(sub_string) > 200:
    print("Length out of range")
else:
    for i in range(0, len(main_string) - len(sub_string) + 1):
        if find_sub_string(i, main_string, sub_string):
            sub_str_cnt += 1
        else:
            continue
    print(str(sub_str_cnt))

