import string

rows, columns = [int(x) for x in input().split()]

matrix = []
alphabet_string = string.ascii_lowercase
alphabet = list(alphabet_string)

for row in range(rows):
    matrix.append([])
    for col in range(columns):
        matrix[row].append(alphabet[row] + alphabet[row + col] + alphabet[row])


for k in matrix:
    print(' '.join(k))




