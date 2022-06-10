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


text = input()
size = int(input())

matrix = []
player_row = 0
player_col = 0
for row in range(size):
    row_elements = input()
    row_elements = list(row_elements)
    for col in range(size):
        if row_elements[col] == 'P':
            player_row = row
            player_col = col
    matrix.append(row_elements)

moves = int(input())

for _ in range(moves):
    command = input()
    matrix[player_row][player_col] = '-'
    next_row, next_col = get_next_pos(player_row, player_col, command)
    player_row, player_col = next_row, next_col

    if is_outside(next_row, next_col, matrix):
        if len(text) > 0:
            text = text[:-1]
            if player_col < 0:
                player_row, player_col = player_row, player_col + 1
            elif player_row < 0:
                player_row, player_col = player_row + 1, player_col
            elif player_row >= len(matrix):
                player_row, player_col = player_row - 1, player_col
            elif player_col >= len(matrix):
                player_row, player_col = player_row, player_col - 1
            matrix[player_row][player_col] = 'P'
        continue

    if matrix[player_row][player_col].isalpha():
        text += matrix[player_row][player_col]
        matrix[player_row][player_col] = 'P'

    if not matrix[player_row][player_col].isalpha():
        matrix[player_row][player_col] = 'P'

print(text)
for row in matrix:
    print(*row, sep='')
