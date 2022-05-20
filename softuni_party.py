def is_vip(guest):
    return guest[0].isdigit()

number_guests = int(input())

vip_list = set()
regular_list = set()

for _ in range(number_guests):
    current_guest = input()
    if is_vip(current_guest):
        vip_list.add(current_guest)
    else:
        regular_list.add(current_guest)

while True:
    shown_guest = input()
    if shown_guest == 'END':
        break
    if is_vip(shown_guest):
        vip_list.remove(shown_guest)
    else:
        regular_list.remove(shown_guest)

total_left = len(vip_list) + len(regular_list)
print(total_left)
[print(guest) for guest in sorted(vip_list)]
[print(guest) for guest in sorted(regular_list)]