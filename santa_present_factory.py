from collections import deque

materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])
crafting_table = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}

presents = {}

while materials and magic_values:
    material = materials.pop()
    value = magic_values.popleft()

    if material == 0 and value == 0:
        continue

    if material == 0:
        magic_values.appendleft(value)
        continue

    if value == 0:
        materials.append(material)
        continue

    result = material * value
    if result in crafting_table:
        toy_name = crafting_table[result]
        if toy_name in presents:
            presents[toy_name] += 1
        else:
            presents[toy_name] = 1
        continue
    if result < 0:
        materials.append(material + value)
    else:
        materials.append(material + 15)


if ('Doll' in presents and 'Wooden train' in presents) or ('Teddy bear' in presents and 'Bicycle' in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(x) for x in reversed(materials)])}")

if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")

for toy, count in sorted(presents.items()):
    print(f'{toy}: {count}')