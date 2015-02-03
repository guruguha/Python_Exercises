__author__ = 'Guruguha'
# List comprehensions
x = input()
y = input()
z = input()
N = input()

def point_generator(x,y,z,N):
    x = int(x)
    y = int(y)
    z = int(z)
    N = int(N)
    point_co_ord = []
    list_of_points = []
    for i in range(0, x+1):
        for j in range(0, y+1):
            sum_ij = i + j
            for k in range(0, z+1):
                sum_jk = j + k
                sum_ik = i + k

                sum_ijk = sum_ij + k
                if sum_ijk != N:
                    point_co_ord.append(i)
                    point_co_ord.append(j)
                    point_co_ord.append(k)
                list_of_points.append(point_co_ord)

                sum_ijk = sum_jk + i
                if sum_ijk != N:
                    point_co_ord.append(i)
                    point_co_ord.append(j)
                    point_co_ord.append(k)
                list_of_points.append(point_co_ord)

                sum_ijk = sum_ik + j
                if sum_ijk != N:
                    point_co_ord.append(i)
                    point_co_ord.append(j)
                    point_co_ord.append(k)
                list_of_points.append(point_co_ord)

    required_points = list_of_points[0]
    group_of_points = [required_points[i:i + 3] for i in range(0, len(required_points), 3)]

    subset_of_points = []
    for i in range(0,len(group_of_points),3):
        subset_of_points .append(group_of_points[i])

    print(subset_of_points)

point_generator(x,y,z,N)