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
matrix = []
player_row = 0
player_col = 0
points = 0
player_path = []
player_lost = False

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'P':
            player_row = row
            player_col = col
            player_path.append([player_row, player_col])
    matrix.append(row_elements)


while points <= 100 and not player_lost:

    direction = input()

    if direction not in ['up', 'down', 'left', 'right']:
        continue

    matrix[player_row][player_col] = 0
    next_row, next_col = get_next_pos(player_row, player_col, direction)

    player_row, player_col = next_row, next_col

    if is_outside(next_row, next_col, matrix):
        if next_row < 0:
            player_row = len(matrix) - 1
            player_col = next_col
        elif next_col < 0:
            player_col = len(matrix) - 1
            player_row = next_row
        elif next_row >= len(matrix):
            player_row = 0
            player_col = next_col
        elif next_col >= len(matrix):
            player_col = 0
            player_row = next_row

    if matrix[player_row][player_col] == 'X':
        points = int(points/2)
        player_lost = True
        player_path.append([player_row, player_col])
        break
    else:
        points += int(matrix[player_row][player_col])
        matrix[player_row][player_col] = 0
        player_path.append([player_row, player_col])
        if points >= 100:
            break

if points >= 100:
    print(f"You won! You've collected {int(points)} coins.")
else:
    print(f"Game over! You've collected {int(points)} coins.")

print("Your path:")
for cords in player_path:
    print(cords)

