def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size

size = int(input())

matrix = []

for _ in range(size):
    matrix.append([int(x)for x in input().split()])

while True:
    line = input()
    if line == 'END':
        break
    line_parts = line.split()

    row, col, value = [int(x) for x in line_parts[1:]]

    if is_outside(row, col, size):
        print('Invalid coordinates')
        continue

    if line_parts[0] == 'Add':
        matrix[row][col] += value

    elif line_parts[0] == 'Subtract':
        matrix[row][col] -= value

for k in matrix:
    print(' '.join(str(x) for x in k))