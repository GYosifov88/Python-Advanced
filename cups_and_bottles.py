from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0


while cups and bottles:
    cup = cups.popleft()
    bottle = bottles.pop()
    result = cup - bottle
    if result <= 0:
        wasted_water += bottle - cup
    else:
        cups.appendleft(result)


if not cups:
    print(f"Bottles: {' '.join([str(x) for x in bottles])}")

if not bottles:
    print(f"Cups: {' '.join([str(x) for x in cups])}")

print(f"Wasted litters of water: {wasted_water}")

