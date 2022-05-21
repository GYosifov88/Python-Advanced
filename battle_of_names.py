number_of_lines = int(input())
counter = 0
odd_set = set()
even_set = set()
for k in range(number_of_lines):
    counter += 1
    char_value = 0
    total = 0
    name = input()
    for ch in name:
        char_value += ord(ch)
    total = int(char_value / counter)
    if total % 2 == 0:
        even_set.add(total)
    else:
        odd_set.add(total)


if sum(odd_set) == sum(even_set):
    combined = map(str, (odd_set | even_set))
    print(', '.join(combined))
elif sum(odd_set) > sum(even_set):
    different = map(str, (odd_set - even_set))
    print(', '.join(different))
elif sum(odd_set) < sum(even_set):
    symetric = map(str, (odd_set ^ even_set))
    print(', '.join(symetric))
