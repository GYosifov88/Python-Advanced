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


def primary(matrix):
    n = len(matrix)
    primary = []
    for i in range(n):
        primary.append(matrix[i][i])
    return ', '.join([str(x) for x in primary])


def secondary(matrix):
    n = len(matrix)
    secondary = []
    for i in range(n):
        secondary.append(matrix[i][n - i - 1])
    return ', '.join([str(x) for x in secondary])


rows = int(input())

matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split(', ')])


print(f"Primary diagonal: {primary(matrix)}. Sum: {primary_diagonal_sum(matrix)}")
print(f"Secondary diagonal: {secondary(matrix)}. Sum: {secondary_diagonal_sum(matrix)}")


# --------SHORT VERSION without functions---------
# size = int(input()
#
# matrix = []
#
# for _ in range(size):
#     matrix.append([int(x) for x in input().split(', ')])
#
# primary = []
#
# secondary = []
#
# for index in range(size):
#     primary.append(matrix[index][index])
#     secondary.append(matrix[index][index - 1 - size])
#
# print(f"Primary diagonal: {', '.join([str(x) for x in primary])}. Sum: {sum(primary)}")
# print(f"Secondary diagonal: {', '.join([str(x) for x in secondary])}. Sum: {sum(secondary)}")

