def find_symbol(matrix, symbol):
    for row_index in range(num):
        for column_index in range(num):
            if matrix[row_index][column_index] == symbol:
               return row_index, column_index


num = int(input())

matrix = []

for i in range(num):
    matrix.append([x for x in input()])

symbol = input()

result = find_symbol(matrix, symbol)

if result:
    row_index, column_index = result
    print(f'({row_index}, {column_index})')
else:
    print(f"{symbol} does not occur in the matrix")


