number_of_elements = int(input())
elements = set()

for i in range (number_of_elements):
    current_elements = input().split(' ')
    for piece in current_elements:
        elements.add(piece)

for el in elements:
    print(el)
    