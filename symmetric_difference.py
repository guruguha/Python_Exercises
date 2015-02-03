__author__ = 'Guruguha'

#Symmetric difference
len1 = input()
list1 = input()
len2 = input()
list2 = input()
list1 = list1.split()
list2 = list2.split()
set_list1 = set(list1)
set_list2 = set(list2)
diff1 = set_list1.difference(set_list2)
diff2 = set_list2.difference(set_list1)
diff_set = diff1.union(diff2)
diff_list = list(diff_set)
diff_list = list(map(int, diff_list))
diff_list.sort()
for i in range(0, len(diff_list)):
    print(diff_list[i])
