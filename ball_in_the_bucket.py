def sumColumn(matrix, column):
    total = 0
    for row in range(len(matrix)):
        total += int(matrix[row][column])
    return total


matrix = []
size = 6
points_gathered = 0
buckets = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'B':
            bucket_row = row
            bucket_col = col
            buckets.append([bucket_row, bucket_col])
    matrix.append(row_elements)

for shot in range(3):
    current_shot = [int(x) for x in input().strip('()').split(', ')]
    shot_row = 0
    shot_col = 0
    if current_shot in buckets:
        shot_row = current_shot[0]
        shot_col = current_shot[1]
        matrix[shot_row][shot_col] = 0
        points_gathered += sumColumn(matrix, shot_col)
        matrix[shot_row][shot_col] = 'B'
        buckets.remove(current_shot)

if points_gathered < 100:
    print(f"Sorry! You need {100 - points_gathered} points more to win a prize.")

elif 100 <= points_gathered <= 199:
    print(f"Good job! You scored {points_gathered} points, and you've won Football.")

elif 200 <= points_gathered <= 299:
    print(f"Good job! You scored {points_gathered} points, and you've won Teddy Bear.")

elif points_gathered >= 300:
    print(f"Good job! You scored {points_gathered} points, and you've won Lego Construction Set.")