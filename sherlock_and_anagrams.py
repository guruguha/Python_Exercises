n = int(input().strip())

for i in range(0,n):
    str_in = str(input().strip())
    str_len = len(str_in)
    unique_substr_set = set()
    anagram_cnt = 0
    for j in range(0, str_len):
        for k in range(j, str_len):
            sub_list = list(str_in[j:k+1])
            sub_list.sort()
            sub_str = ''.join(sub_list)
            print(sub_str)
            if sub_str in unique_substr_set:
                anagram_cnt += 1
            else:
                unique_substr_set.add(sub_str)

    print(anagram_cnt)
