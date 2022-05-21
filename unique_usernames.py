number_of_usernames = int(input())

usernames = set()

for _ in range(number_of_usernames):
    current_username = input()
    usernames.add(current_username)

for name in usernames:
    print(name)
