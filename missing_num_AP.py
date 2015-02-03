__author__ = 'Guruguha'

# Enter your code here. Read input from STDIN. Print output to STDOUT
num_inputs = int(input())
num_str = input()
num_list = num_str.split(' ')

diff = []

for x in range(0, len(num_list)-1):
    diff.append(int(num_list[x+1]) - int(num_list[x]))

for x in range(0, len(diff)-1):
    if diff[x] > 0:
        if diff[x+1] >= diff[x]:
            cd = diff[x]
            break
        elif diff[x+1] < diff[x]:
            cd = diff[x+1]
            break
    else:
        if diff[x+1] <= diff[x]:
            cd = diff[x]
            break
        elif diff[x+1] > diff[x]:
            cd = diff[x+1]
            break
for x in range(0, len(diff)-1):
    if cd > 0:
        if diff[x+1] > diff[x]:
            missing_idx = x+1
            print(missing_idx)
            missing_num = int(num_list[missing_idx]) + cd
            break
        else:
            missing_idx = x
            missing_num = int(num_list[missing_idx]) + cd
            break
    else:
        if diff[x+1] < diff[x]:
            missing_idx = x+1
            missing_num = int(num_list[missing_idx]) + cd
            break
        else:
            missing_idx = x
            missing_num = int(num_list[missing_idx]) + cd
            break
for i in range(0, len(num_list)-1):
    if int(num_list[i + 1]) != int(num_list[i]) + cd:
        missing_num = int(num_list[i]) + cd
print(missing_num)

