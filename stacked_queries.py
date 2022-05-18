stack = []
reversed_list = []
number = int(input())

for _ in range(number):
    command = input().split(' ')
    if command[0] == '1':
        num = int(command[1])
        stack.append(num)
    elif command[0] == '2':
        if len(stack) > 0:
            stack.pop()
    elif command[0] == '3':
        if len(stack) > 0:
            max_num = max(stack)
            print(max_num)
    elif command[0] == '4':
        if len(stack) > 0:
            min_num = min(stack)
            print(min_num)

for i in range(len(stack)):
    reversed_list.append(stack.pop())

reversed_list_str = [str(i) for i in reversed_list]
print(", ".join(reversed_list_str))
