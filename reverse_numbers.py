initial_list = list(input().split(' '))
reversed_list = []
for i in range(len(initial_list)):
    reversed_list.append(initial_list.pop())

print(" ".join(reversed_list))