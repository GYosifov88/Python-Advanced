from collections import deque

chocolates = input().split(', ')
cup_of_milks = input().split(', ')
milkshakes = 0
chocolates_int = [int(x) for x in chocolates]
cup_of_milks_int = deque(map(int, cup_of_milks))

while len(chocolates_int) > 0 and len(cup_of_milks_int) > 0 and milkshakes < 5:
    chocolate = chocolates_int.pop()
    milk = cup_of_milks_int.popleft()
    if chocolate <= 0 and milk <= 0:
        continue
    if chocolate <= 0:
        cup_of_milks_int.appendleft(milk)
        continue
    if milk <= 0:
        chocolates_int.append(chocolate)
        continue
    if chocolate == milk:
        milkshakes += 1
    else:
        cup_of_milks_int.append(milk)
        chocolates_int.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates_int:
    chocolates_left = [str(x) for x in chocolates_int]
    print(f"Chocolate: {', '.join(chocolates_left)}")
else:
    print("Chocolate: empty")

if cup_of_milks_int:
    cup_of_milks_left = [str(x) for x in cup_of_milks_int]
    print(f"Milk: {', '.join(cup_of_milks_left)}")
else:
    print("Milk: empty")
