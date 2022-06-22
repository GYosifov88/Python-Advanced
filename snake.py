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


size = int(input())
burrows = []
matrix = []
snake_row = 0
snake_col = 0
gathered_food = 0
get_outside = False
for row in range(size):
    row_elements = [x for x in input()]
    for col in range(size):
        if row_elements[col] == 'S':
            snake_row = row
            snake_col = col
        if row_elements[col] == 'B':
            burrow_row = row
            burrow_col = col
            burrows.append([burrow_row, burrow_col])
    matrix.append(row_elements)

while gathered_food < 10:

    direction = input()

    next_row, next_col = get_next_pos(snake_row, snake_col, direction)

    if is_outside(next_row, next_col, matrix):
        matrix[snake_row][snake_col] = '.'
        get_outside = True
        break
    matrix[snake_row][snake_col] = '.'
    snake_row, snake_col = next_row, next_col

    if matrix[snake_row][snake_col] == '*':
        gathered_food += 1
        matrix[snake_row][snake_col] = 'S'
    elif matrix[snake_row][snake_col] == 'B':
        matrix[snake_row][snake_col] = '.'
        burrows.remove([snake_row, snake_col])
        snake_row, snake_col = burrows[0]


if get_outside:
    print("Game over!")
    print(f"Food eaten: {gathered_food}")
if gathered_food >= 10:
    print("You won! You fed the snake.")
    print(f"Food eaten: {gathered_food}")
for row in matrix:
    print(*row, sep='')