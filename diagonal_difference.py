def primary_diagonal_sum(matrix):
    sum = 0
    n = len(matrix)
    for i in range(n):
        sum += matrix[i][i]
    return sum


def secondary_diagonal_sum(matrix):
    sum = 0
    n = len(matrix)
    for i in range(n):
        sum += matrix[i][n - i - 1]
    return sum


rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(' ')])

difference = abs(primary_diagonal_sum(matrix) - secondary_diagonal_sum(matrix))

print(difference)
