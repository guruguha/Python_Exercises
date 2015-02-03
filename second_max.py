__author__ = 'Guruguha'

# Second max
def find_max(input_array):
    max = input_array[0]
    for i in input_array:
        if int(i) > int(max):
            max = i
    return max

num = input()
input_values = []

input_values = input()
input_array = input_values.split()
max1 = find_max(input_array)
input_array.remove(max1)
max2 = find_max(input_array)
while max1 == max2:
    max2 = find_max(input_array)
    input_array.remove(max2)
else:
    print(max2)

