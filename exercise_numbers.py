first = set([int(x) for x in input().split(' ')])
second = set([int(x) for x in input().split(' ')])

number = int(input())

for _ in range(number):
    current_action = input().split(' ')
    command = current_action[0]
    targe_set = current_action[1]
    if command == 'Add':
        if targe_set == 'First':
            first = first.union([int(x) for x in current_action[2:]])
        else:
            second = second.union([int(x) for x in current_action[2:]])

    elif command == 'Remove':
        if targe_set == 'First':
            first = first.difference([int(x) for x in current_action[2:]])
        else:
            second = second.difference([int(x) for x in current_action[2:]])

    elif command == 'Check':
        if first.issubset(second) or second.issubset(first):
            print('True')
        else:
            print('False')

first_sorted = sorted(first)
second_sorted = sorted(second)
print(*first_sorted, sep=', ')
print(*second_sorted, sep=', ')
