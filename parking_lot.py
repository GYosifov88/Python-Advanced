number_of_cars = int(input())

parking_lot = set()

for _ in range(number_of_cars):
    command, current_car = input().split(', ')
    if command == 'IN':
        parking_lot.add(current_car)
    elif command == 'OUT':
        parking_lot.remove(current_car)

if parking_lot:
    for car in parking_lot:
        print(car)
else:
    print("Parking Lot is Empty")