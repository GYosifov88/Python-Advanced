import re
initial_list = input().split('|')

result = []

for idx in range(len(initial_list) -1, -1, -1):
    current_element = initial_list[idx].strip().split()
    result.extend(current_element)

print(' '.join(result))