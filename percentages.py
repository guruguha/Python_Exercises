__author__ = 'Guruguha'

# Percentages
num_of_students = int(input())
if num_of_students < 2 or num_of_students > 10:
    print("Enter valid number of students")
else:
    count = num_of_students
    student_data = []

    valid_input = True
    while count != 0:
        values = input()
        input_list = values.split()
        if input_list[1].isdigit() is False or float(input_list[1]) < 0 or float(input_list[1]) > 100:
            print("Enter valid marks for physics")
            valid_input = False
        if input_list[2].isdigit() is False or float(input_list[2]) < 0 or float(input_list[2]) > 100:
            print("Enter valid marks for chemistry")
            valid_input = False
        if input_list[3].isdigit() is False or float(input_list[3]) < 0 or float(input_list[3]) > 100:
            print("Enter valid marks for mathematics")
            valid_input = False

        dict = {'name':input_list[0], 'physics':input_list[1], 'chemistry':input_list[2], 'mathematics':input_list[3]}
        student_data.append(dict)
        count -= 1

    if valid_input:
        search_student = input()
        for i in range(0, len(student_data)):
            if search_student == student_data[i]['name']:
                total_marks = float(student_data[i]['physics']) \
                              + float(student_data[i]['chemistry'])\
                              + float(student_data[i]['mathematics'])
                avg = total_marks / 3
                print(str("{0:.2f}".format(avg)))
                break
    else:
        print("Invalid input")

