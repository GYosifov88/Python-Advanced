def get_magic_triangle(num):
    triangle = []  # an empty list
    for n in range(num):
        triangle.append([])
        triangle[n].append(1)
        for m in range(1, n):
            triangle[n].append(triangle[n - 1][m - 1] + triangle[n - 1][m])
        if n != 0:
            triangle[n].append(1)
    return triangle

get_magic_triangle(5)

