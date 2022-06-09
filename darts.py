def sumColumn(matrix, row, column):
    total = 0
    for row in range(len(matrix)):
        if matrix[row][column].isdigit():
            total += int(matrix[row][column])
    for digit in matrix[shot_row]:
        if digit.isdigit():
            total += int(digit)
    return total


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


first_player, second_player = input().split(', ')

matrix = []
size = 7
first_player_points = 501
second_player_points = 501
first_player_shots = 0
second_player_shots = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'B':
            bull_row = row
            bull_col = col
    matrix.append(row_elements)

counter = 1
while first_player_points > 0 or second_player_points > 0:
    coordinates = [int(x) for x in input().strip('()').split(', ')]
    if counter % 2 != 0:
        shot_row = coordinates[0]
        shot_col = coordinates[1]
        first_player_shots += 1

        if is_outside(shot_row, shot_col, len(matrix)):
            counter += 1
            continue

        if matrix[shot_row][shot_col] == 'B':
            print(f"{first_player} won the game with {first_player_shots} throws!")
            break
        if matrix[shot_row][shot_col] != 'B' and matrix[shot_row][shot_col] != 'D' and matrix[shot_row][shot_col] != 'T':
            first_player_points -= int(matrix[shot_row][shot_col])

        if matrix[shot_row][shot_col] == 'D':
            sum = 0
            sum += sumColumn(matrix, shot_row, shot_col)
            first_player_points -= sum * 2
        if matrix[shot_row][shot_col] == 'T':
            sum = 0
            sum += sumColumn(matrix, shot_row, shot_col)
            first_player_points -= sum * 3
        if first_player_points <= 0:
            print(f"{first_player} won the game with {first_player_shots} throws!")
            break
    if counter % 2 == 0:
        shot_row = coordinates[0]
        shot_col = coordinates[1]
        second_player_shots += 1
        if is_outside(shot_row, shot_col, len(matrix)):
            counter +=1
            continue

        if matrix[shot_row][shot_col] == 'B':
            print(f"{second_player} won the game with {second_player_shots} throws!")
            break
        if matrix[shot_row][shot_col] != 'B' and matrix[shot_row][shot_col] != 'D' and matrix[shot_row][shot_col] != 'T':
            second_player_points -= int(matrix[shot_row][shot_col])

        if matrix[shot_row][shot_col] == 'D':
            sum = 0
            sum += sumColumn(matrix, shot_row, shot_col)
            second_player_points -= sum * 2
        if matrix[shot_row][shot_col] == 'T':
            sum = 0
            sum += sumColumn(matrix, shot_row, shot_col)
            second_player_points -= sum * 3
        if second_player_points <= 0:
            print(f"{second_player} won the game with {second_player_shots} throws!")
            break
    counter += 1

