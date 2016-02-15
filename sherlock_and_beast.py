import re
t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    # fives = n
    # threes =0
    max_num = int("9" * n)
    fives_and_threes = {3:True, 5:True}

    for i in range(max_num, 0, -1):
        tmp = str(i)
        fives = 0
        threes = 0
        if not re.search(r'^[53]+$', tmp):
            continue
        else:
            fives = 0
            threes = 0
            num_digits = 0
            int_v = i
            int_v = 33333
            while int_v > 0:
                num_digits += 1
                rem = int_v % 10
                int_v = int(int_v/10)
                if rem == 5:
                    fives += 1
                else:
                    threes += 1
            if fives % 3 == 0 and threes % 5 == 0:
                print(i)
        # if(has_only_fives_and_threes(fives_and_threes, tmp)):
        #     for s in tmp:
        #         if s == '5':
        #             fives += 1
        #         elif s == '3':
        #             threes += 1
        #
        #     if fives % 3 == 0 and threes % 5 == 0:
        #         print(i)
            # int_v = i
            # fives = 0
            # threes = 0
            # num_digits = 0
            # while int_v >= 0:
            #     num_digits += 1
            #     rem = int_v % 10
            #     int_v = int(int_v/10)
            #     if rem not in [3,5]:
            #         fives = 0
            #         threes = 0
            #         print("-1")
            #         break
            #     else:
            #         if rem == 5:
            #             fives += 1
            #         else:
            #             threes += 1
            # if num_digits == fives + threes:
            #     if fives % 3 == 0 and threes % 5 == 0:
            #         print(i)
