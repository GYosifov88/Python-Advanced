def read_matrix():
    number = int(input())
    matrix = []
    for _ in range(number):
        digits = [int(x) for x in input().split(', ')]
        matrix.append(digits)
    return matrix

matrix = read_matrix()

result = [
    x for i in matrix for x in i
]
print(result)