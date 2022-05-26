rows, columns = [int(x) for x in input().split(', ')]
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

column_sum = [0] * columns

for row in range(rows):
    for column in range(columns):
        column_sum[column] += matrix[row][column]

[print(x) for x in column_sum]
