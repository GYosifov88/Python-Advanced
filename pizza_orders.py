from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employees_capacity = [int(x) for x in input().split(', ')]

total_pizzas_made = 0

while pizza_orders and employees_capacity:
    current_pizza = pizza_orders.popleft()

    if current_pizza <= 0:
        continue

    if current_pizza > 10:
        continue

    current_employee = employees_capacity.pop()

    if current_pizza <= current_employee:
        total_pizzas_made += current_pizza
    elif current_pizza > current_employee:
        current_pizza -= current_employee
        total_pizzas_made += current_employee
        pizza_orders.appendleft(current_pizza)


if len(pizza_orders) <= 0:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    print(f"Employees: {', '.join(str(x) for x in employees_capacity)}")
    
if len(pizza_orders) > 0 and len(employees_capacity) <=0:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")