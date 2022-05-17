from collections import deque

people = deque()

initial_water = int(input())

while True:
    command = input()
    if command == 'Start':
        break
    else:
        people.append(command)

while True:
    command = input()
    if command == 'End':
        break
    elif command.startswith('refill '):
        current_command = command.split(' ')
        initial_water += int(current_command[1])
    else:
        person = people.popleft()
        liters = int(command)
        if liters <= initial_water:
            initial_water -= liters
            print(f'{person} got water')
        else:
            print(f'{person} must wait')

print(f'{initial_water} liters left')
