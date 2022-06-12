from collections import deque

fireworks = deque(int(x) for x in input().split(', '))
explosive_powers = [int(x) for x in input().split(', ')]
palm = 0
willow = 0
crossette = 0
all_gathered = False

while fireworks and explosive_powers:
    current_firework = fireworks[0]
    current_explosive_power = explosive_powers[-1]

    if current_firework <= 0:
        fireworks.popleft()
        continue
    if current_explosive_power <= 0:
        explosive_powers.pop()
        continue

    if (current_firework + current_explosive_power) % 3 == 0 and (current_firework + current_explosive_power) % 5 != 0:
        palm += 1
        fireworks.popleft()
        explosive_powers.pop()
    elif (current_firework + current_explosive_power) % 5 == 0 and (current_firework + current_explosive_power) % 3 != 0:
        willow += 1
        fireworks.popleft()
        explosive_powers.pop()
    elif (current_firework + current_explosive_power) % 5 == 0 and (current_firework + current_explosive_power) % 3 == 0:
        crossette += 1
        fireworks.popleft()
        explosive_powers.pop()
    else:
        current_firework = fireworks.popleft() - 1
        fireworks.append(current_firework)

    if willow >= 3 and crossette >= 3 and palm >= 3:
        all_gathered = True
        break


if all_gathered:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks)}")
if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")

print(f"Palm Fireworks: {palm}")
print(f"Willow Fireworks: {willow}")
print(f"Crossette Fireworks: {crossette}")


