from collections import deque

food_quantity = int(input())

orders = deque(input().split(' '))
orders_int = deque(int(i) for i in orders)
print(max(orders_int))

for i in orders_int:
    if food_quantity >= i:
        food_quantity -= i
        orders.popleft()
    else:
        break

if len(orders) == 0:
    print('Orders complete')
else:
    print(f"Orders left: ", end='' ' '.join(orders))
