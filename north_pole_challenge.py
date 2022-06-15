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
    return row < 0 or col < 0 or row >= rows or col >= columns


rows, columns = [int(x) for x in input().split(', ')]
matrix = []
decorations = 0
gifts = 0
cookies = 0
collected_decorations = 0
collected_gifts = 0
collected_cookies = 0
my_row = 0
my_col = 0
all_gathered = False

for row in range(rows):
    row_elements = input().split()
    for col in range(columns):
        if row_elements[col] == 'Y':
            my_row = row
            my_col = col
        if row_elements[col] == 'D':
            decorations += 1
        if row_elements[col] == 'G':
            gifts += 1
        if row_elements[col] == 'C':
            cookies += 1
    matrix.append(row_elements)


while not all_gathered:
    command = input()
    if command == 'End' or all_gathered:
        break

    direction, steps = command.split('-')
    steps_int = int(steps)

    for c in range(1, steps_int + 1):
        next_row, next_col = get_next_pos(my_row, my_col, direction)
        if decorations == 0 and gifts == 0 and cookies == 0:
            matrix[my_row][my_col] = 'Y'
            all_gathered = True
            break
        else:
            matrix[my_row][my_col] = 'x'
            my_row, my_col = next_row, next_col

        if is_outside(next_row, next_col, matrix):
            if next_row < 0:
                my_row = rows - 1
                my_col = next_col
            elif next_col < 0:
                my_col = columns - 1
                my_row = next_row
            elif next_row >= rows:
                my_row = 0
                my_col = next_col
            elif next_col >= columns:
                my_col = 0
                my_row = next_row
        if matrix[my_row][my_col] == 'D':
            decorations -= 1
            collected_decorations += 1
            matrix[my_row][my_col] = 'Y'
        if matrix[my_row][my_col] == 'C':
            cookies -= 1
            collected_cookies += 1
            matrix[my_row][my_col] = 'Y'
        if matrix[my_row][my_col] == 'G':
            gifts -= 1
            collected_gifts += 1
            matrix[my_row][my_col] = 'Y'
        if matrix[my_row][my_col] == '.':
            matrix[my_row][my_col] = 'Y'
        if matrix[my_row][my_col] == 'x':
            matrix[my_row][my_col] = 'Y'
        if c % steps_int == 1:
            matrix[my_row][my_col] = 'Y'
        if decorations == 0 and gifts == 0 and cookies == 0:
            all_gathered = True
            break


if all_gathered:
    print("Merry Christmas!")
    print("You've collected:")
    print(f"- {collected_decorations} Christmas decorations")
    print(f"- {collected_gifts} Gifts")
    print(f"- {collected_cookies} Cookies")

    for row in matrix:
        print(*row, sep=' ')
else:
    print("You've collected:")
    print(f"- {collected_decorations} Christmas decorations")
    print(f"- {collected_gifts} Gifts")
    print(f"- {collected_cookies} Cookies")

    for row in matrix:
        print(*row, sep=' ')