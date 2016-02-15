t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    int_v = n
    divisible_count = 0
    visited_numbers = set()
    while int_v > 0:
        rem = int_v % 10
        int_v = int(int_v/10)
        if rem != 0 and (n % rem == 0):
            divisible_count += 1
    print(divisible_count)
