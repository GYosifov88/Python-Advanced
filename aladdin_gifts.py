from collections import deque

presents_materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
presents = {'Gemstone': 0, 'Porcelain Sculpture': 0, 'Gold': 0, 'Diamond Jewellery': 0}
success = False

while presents_materials and magic_levels:
    current_material = presents_materials.pop()
    current_magic = magic_levels.popleft()

    if 100 <= (current_magic + current_material) <= 499:
        if 100 <= (current_magic + current_material) <= 199:
            presents['Gemstone'] += 1
        elif 200 <= (current_magic + current_material) <= 299:
            presents['Porcelain Sculpture'] += 1
        elif 300 <= (current_magic + current_material) <= 399:
            presents['Gold'] += 1
        elif 400 <= (current_magic + current_material) <= 499:
            presents['Diamond Jewellery'] += 1

    if (current_magic + current_material) < 100:
        if (current_magic + current_material) % 2 == 0:
            current_material = current_material * 2
            current_magic = current_magic * 3
            if 100 <= (current_magic + current_material) <= 499:
                if 100 <= (current_magic + current_material) <= 199:
                    presents['Gemstone'] += 1
                elif 200 <= (current_magic + current_material) <= 299:
                    presents['Porcelain Sculpture'] += 1
                elif 300 <= (current_magic + current_material) <= 399:
                    presents['Gold'] += 1
                elif 400 <= (current_magic + current_material) <= 499:
                    presents['Diamond Jewellery'] += 1
        elif (current_magic + current_material) % 2 != 0:
            current_material = current_material * 2
            current_magic = current_magic * 2
            if 100 <= (current_magic + current_material) <= 499:
                if 100 <= (current_magic + current_material) <= 199:
                    presents['Gemstone'] += 1
                elif 200 <= (current_magic + current_material) <= 299:
                    presents['Porcelain Sculpture'] += 1
                elif 300 <= (current_magic + current_material) <= 399:
                    presents['Gold'] += 1
                elif 400 <= (current_magic + current_material) <= 499:
                    presents['Diamond Jewellery'] += 1

    if (current_magic + current_material) > 499:
        current_magic = current_magic / 2
        current_material = current_material / 2
        if 100 <= (current_magic + current_material) <= 499:
            if 100 <= (current_magic + current_material) <= 199:
                presents['Gemstone'] += 1
            elif 200 <= (current_magic + current_material) <= 299:
                presents['Porcelain Sculpture'] += 1
            elif 300 <= (current_magic + current_material) <= 399:
                presents['Gold'] += 1
            elif 400 <= (current_magic + current_material) <= 499:
                presents['Diamond Jewellery'] += 1

if (presents['Gemstone'] >= 1 and presents['Porcelain Sculpture'] >= 1) or (presents['Gold'] >= 1 and presents['Diamond Jewellery'] >= 1):
    success = True

presents = {key: value for key, value in presents.items() if value != 0}
sorted_dict = {k: presents[k] for k in sorted(presents)}

if success:
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if presents_materials:
    print(f"Materials left: {', '.join(str(x) for x in presents_materials)}")
if magic_levels:
    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

for present in sorted_dict.keys():
    print(f"{present}: {sorted_dict[present]}")
    