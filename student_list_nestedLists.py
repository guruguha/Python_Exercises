__author__ = 'Guruguha'

from operator import itemgetter
# Nested list

student_list = []
num_of_students = input()
cnt = 0
while cnt < int(num_of_students):
    name = input()
    marks = input()
    student = []
    student.append(name)
    student.append(float(marks))

    student_list.append(student)
    cnt += 1

student_list.sort(key=itemgetter(1))

cnt = 0
while student_list[cnt][1] == student_list[cnt + 1][1]:
    cnt += 1
cnt += 1

req_ids = [cnt]
while cnt != (len(student_list) - 1) and student_list[cnt][1] == student_list[cnt + 1][1]:
    req_ids.append(cnt + 1)
    cnt += 1

if cnt != 1:
    same_grades = []
    for i in req_ids:
        same_grades.append(student_list[i][0])
    same_grades.sort(key=itemgetter(0))

    for j in range(0, len(same_grades)):
        print(same_grades[j])
else:
    print(student_list[1][0])

