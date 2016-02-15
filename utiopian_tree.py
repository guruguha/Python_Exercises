t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    initial_height = 1
    curr_season = "spring"
    final_height = initial_height
    for i in range(n):
        if curr_season == "spring":
            final_height *= 2
            curr_season = "summer"
        elif curr_season == "summer":
            final_height += 1
            curr_season = "spring"

    print(final_height)
