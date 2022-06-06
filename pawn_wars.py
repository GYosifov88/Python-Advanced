def white_capture(row, col):
    possible_moves = \
        {
            'up left': (row - 1, col - 1),
            'up right': (row - 1, col + 1)
        }
    for key in possible_moves.keys():
        current_row, current_col = possible_moves[key]
        if 0 <= current_col < 8:
            if matrix[current_row][current_col] == matrix[black_row][black_col]:
                return True


def black_capture(row, col):
    possible_moves = \
        {
            'up left': (row + 1, col - 1),
            'up right': (row + 1, col + 1)
        }
    for key in possible_moves.keys():
        current_row, current_col = possible_moves[key]
        if 0 <= current_col < 8:
            if matrix[current_row][current_col] == matrix[white_row][white_col]:
                return True

size = 8
matrix = []
white_row = 0
white_col = 0
black_row = 0
black_col = 0
black_win = False
white_win = False
number = 8

for row in range(size):
    row_elements = input().split()
    char_num = 97
    for col in range(size):
        if row_elements[col] == 'w':
            white_row = row
            white_col = col
        elif row_elements[col] == 'b':
            black_row = row
            black_col = col
        row_elements[col] = f'{chr(char_num)}{number}'
        char_num += 1
    number -= 1
    matrix.append(row_elements)


while True:
    if matrix[white_row][white_col] in ['a8', 'b8', 'c8', 'd8', 'e8', 'f8', 'g8', 'h8']:
        print(f'Game over! White pawn is promoted to a queen at {matrix[white_row][white_col]}.')
        break
    if matrix[black_row][black_col] in ['a1', 'b1', 'c1', 'd1', 'f1', 'e1', 'g1', 'h1']:
        print(f'Game over! Black pawn is promoted to a queen at {matrix[black_row][black_col]}.')
        break
    if white_capture(white_row, white_col):
        print(f'Game over! White win, capture on {matrix[black_row][black_col]}.')
        break
    white_row -= 1
    if black_capture(black_row, black_col):
        print(f'Game over! Black win, capture on {matrix[white_row][white_col]}.')
        break
    black_row += 1

