from collections import deque

green_light_duration = int(input())
free_window = int(input())

queue = deque()
passed_cars = 0
hitted = False

while True:
    command = input()
    if command == 'END' or hitted:
        break
    elif command != 'green' and command != 'END':
        queue.append(command)

    elif command == 'green':
        current_time = green_light_duration
        while queue and current_time > 0:
            current_car = queue[0]
            current_car_lenght = len(current_car)
            if current_car_lenght <= current_time:
                passed_cars += 1
                queue.popleft()
                current_time -= current_car_lenght
                if current_time == 0:
                    break

            elif 0 < current_time <= current_car_lenght:
                if current_time + free_window >= current_car_lenght:
                    passed_cars += 1
                    queue.popleft()
                    break
                else:
                    hitted = True
                    hitted_part = current_car[current_time+free_window]
                    print("A crash happened!")
                    print(f"{current_car} was hit at {hitted_part}.")
                    break

if not hitted:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
