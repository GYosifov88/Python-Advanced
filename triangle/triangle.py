from Modules.triangle.line import print_line


def print_triangle(size):
    for row in range(size):
        print_line(row + 1)

    for row in range(size - 2 , -1, -1):
        print_line(row + 1)