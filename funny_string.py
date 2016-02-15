num_inputs = int(input().strip())


def find_funny(input_str, str_len):

    for i in range(1, str_len):
        ascii_l = abs(ord(input_str[i]) - ord(input_str[i-1]))
        ascii_r = abs(ord(input_str[str_len - i]) - ord(input_str[str_len - i - 1]))

        if ascii_l != ascii_r:
            return False
    return True

for num in range(0,num_inputs):
    input_str = str(input().strip())
    str_len = len(input_str)

    is_funny = find_funny(input_str, str_len)
    if is_funny:
        print("Funny")
    else:
        print("Not Funny")
