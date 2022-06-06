from collections import deque


def get_next_pos(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


def is_outside(row, col, matrix):
    return row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix)


size = 6
matrix = []
water = 0
metal = 0
concrete = 0
rover_row = 0
rover_col = 0
broken = False

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'E':
            rover_row = row
            rover_col = col
    matrix.append(row_elements)

commands = deque(input().split(', '))

while commands:
    direction = commands.popleft()

    next_row, next_col = get_next_pos(rover_row, rover_col, direction)

    rover_row, rover_col = next_row, next_col

    if is_outside(next_row ,next_col ,matrix):
        if next_row < 0:
            rover_row = len(matrix) - 1
            rover_col = next_col
        elif next_col < 0:
            rover_col = len(matrix) - 1
            rover_row = next_row
        elif next_row >= len(matrix):
            rover_row = 0
            rover_col = next_col
        elif next_col >= len(matrix):
            rover_col = 0
            rover_row = next_row


    if matrix[rover_row][rover_col] == 'W':
        water += 1
        print(f"Water deposit found at ({rover_row}, {rover_col})")

    if matrix[rover_row][rover_col] == 'M':
        metal += 1
        print(f"Metal deposit found at ({rover_row}, {rover_col})")

    if matrix[rover_row][rover_col] == 'C':
        concrete += 1
        print(f"Concrete deposit found at ({rover_row}, {rover_col})")

    if matrix[rover_row][rover_col] == 'R':
        print(f"Rover got broken at ({rover_row}, {rover_col})")
        broken = True
        break

if not commands or broken:
    if metal != 0 and concrete != 0 and water != 0:
        print("Area suitable to start the colony.")
    else:
        print("Area not suitable to start the colony.")
