clothes_box = input().split(' ')
clothes_box_int = list(int(i) for i in clothes_box)
rack_capacity = int(input())
current_rack = rack_capacity
counter = 1

while clothes_box_int:
    piece_of_clothing = clothes_box_int[-1]
    if piece_of_clothing > current_rack:
        counter += 1
        current_rack = rack_capacity
    else:
        current_rack -= piece_of_clothing
        clothes_box_int.pop()

print(counter)
