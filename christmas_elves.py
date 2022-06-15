from collections import deque

elfs_energy = deque(int(x) for x in input().split())
box_with_materials = [int(x) for x in input().split()]

toys_made = 0
energy_used = 0
counter = 0
while elfs_energy and box_with_materials:
    current_elf = elfs_energy.popleft()
    if current_elf < 5:
        continue
    counter += 1
    current_box = box_with_materials.pop()
    if counter % 5 == 0 and counter % 3 == 0:
        if current_elf >= current_box * 2:
            energy_used += current_box * 2
            current_elf = current_elf - (current_box * 2)
            elfs_energy.append(current_elf)
        else:
            current_elf = current_elf * 2
            elfs_energy.append(current_elf)
            box_with_materials.append(current_box)

    elif counter % 3 == 0 and counter % 5 != 0:
        if current_elf >= current_box * 2:
            toys_made += 2
            energy_used += current_box * 2
            current_elf = current_elf - (current_box * 2) + 1
            elfs_energy.append(current_elf)
        else:
            current_elf = current_elf * 2
            elfs_energy.append(current_elf)
            box_with_materials.append(current_box)
    elif counter % 5 == 0 and counter % 3 != 0:
        if current_elf >= current_box:
            energy_used += current_box
            current_elf -= current_box
            elfs_energy.append(current_elf)
        elif current_elf < current_box:
            current_elf *= 2
            box_with_materials.append(current_box)
            elfs_energy.append(current_elf)

    else:
        if current_elf >= current_box:
            toys_made += 1
            energy_used += current_box
            current_elf = current_elf - current_box + 1
            elfs_energy.append(current_elf)
        else:
            current_elf *= 2
            elfs_energy.append(current_elf)
            box_with_materials.append(current_box)


print(f"Toys: {toys_made}")
print(f"Energy: {energy_used}")
if elfs_energy:
    print(f"Elves left: {', '.join(str(x) for x in elfs_energy)}")
if box_with_materials:
    print(f"Boxes left: {', '.join(str(x) for x in box_with_materials)}")

