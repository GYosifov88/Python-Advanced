lenghts = [int(x) for x in input().split(' ')]
n = lenghts[0]
m = lenghts[1]
first_set = set()
second_set = set()
common_set = set()
counter = 0
for i in range(n+m):
    counter += 1
    number = int(input())
    if 1 <= counter <= n:
        first_set.add(number)
    elif n < counter <= (n+m):
        second_set.add(number)

common_set = first_set & second_set

for num in common_set:
    print(num)