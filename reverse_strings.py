original_string = input()

stack = []

for c in original_string:
    stack.append(c)

reversed_string = ''

while stack:
    value = stack[-1]
    reversed_string += value
    stack.pop()

print(reversed_string)