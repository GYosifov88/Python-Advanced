numbers_string = input().split(' ')
numbers = [int(x) for x in numbers_string]
target_number = int(input())
values_map = {}
counter = 0

for i1 in range(len(numbers)):
    for i2 in range(i1 + 1, len(numbers)):
        counter += 1
        p1 = numbers[i1]
        p2 = numbers[i2]
        if p1 + p2 == target_number:
            values_map[p1] = p2
            print(f'{p1} + {p2} = {target_number}')


print(f"Iterations done: {counter}")

for pair in values_map.items():
    print(pair)
