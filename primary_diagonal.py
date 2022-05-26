def primary_diagonal_sum(matrix):
    sum = 0
    n = len(matrix)
    for i in range(n):
        sum += matrix[i][i]
    return sum

number = int(input())
matrix = []

for _ in range(number):
    matrix.append([int(x) for x in input().split(' ')])

print(primary_diagonal_sum(matrix))