numbers_string = input()
numbers = [float(x) for x in numbers_string.split(' ')]
occurences = {}

for number in numbers:
    if number not in occurences:
        occurences[number] = 0
    occurences[number] += 1

for number, counts in occurences.items():
    print(f"{number} - {counts} times")
