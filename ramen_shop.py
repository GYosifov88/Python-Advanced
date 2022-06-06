from collections import deque

bowls_of_ramen = [int(x) for x in input().split(', ')]
customers = deque(int(x) for x in input().split(', '))

while bowls_of_ramen and customers:
    current_bow = bowls_of_ramen[-1]
    current_cust = customers[0]

    if current_bow == current_cust:
        customers.popleft()
        bowls_of_ramen.pop()

    elif current_bow > current_cust:
        bowls_of_ramen[-1] -= current_cust
        customers.popleft()
        continue

    elif current_bow < current_cust:
        customers[0] -= current_bow
        bowls_of_ramen.pop()
        continue


if not customers:
    print("Great job! You served all the customers.")
    if bowls_of_ramen:
        print(f"Bowls of ramen left: {', '.join(str(x) for x in bowls_of_ramen)}")

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(x) for x in customers)}")