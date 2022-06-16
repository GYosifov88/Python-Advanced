def get_bombs(matrix, row, col):
    possible_bomb_cords = [
        [row - 1, col - 1],
        [row - 1, col],
        [row - 1, col + 1],
        [row, col - 1],
        [row, col + 1],
        [row + 1, col - 1],
        [row + 1, col],
        [row + 1, col + 1]
    ]
    result = 0
    for current_row, current_col in possible_bomb_cords:
        if 0 <= current_row < len(matrix) and 0 <= current_col < len(matrix) and matrix[current_row][current_col] == '*':
            result += 1

    return result


field_size = int(input())
number_of_bombs = int(input())
matrix = []

for row in range(field_size):
    matrix.append([])
    for col in range(field_size):
        matrix[row].append(0)

for i in range(number_of_bombs):
    bomb_row, bomb_col = [int(x) for x in input().strip('()').split(',')]
    matrix[bomb_row][bomb_col] = '*'

for row in range(len(matrix)):
    for col in range(len(matrix)):
        if matrix[row][col] != '*':
            matrix[row][col] += get_bombs(matrix, row, col)


for row in matrix:
    print(*row, sep=' ')
