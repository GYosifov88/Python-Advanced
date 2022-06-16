from collections import deque

customers = deque(int(x) for x in input().split(', '))
taxis = [int(x) for x in input().split(', ')]
total_time = 0

while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis[-1]

    if current_customer <= current_taxi:
        total_time += current_customer
        taxis.pop()
        customers.popleft()

    else:
        taxis.pop()

if not customers:
    print("All customers were driven to their destinations")
    print(f"Total time: {total_time} minutes")

if not taxis and len(customers) > 0:
    print("Not all customers were driven to their destinations")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")