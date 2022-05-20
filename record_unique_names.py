number_of_names = int(input())

unique_list = set()

for _ in range(number_of_names):
    current_name = input()
    unique_list.add(current_name)

for name in unique_list:
    print(name)
