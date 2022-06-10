from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

matches = 0

while males and females:
    current_male = males.pop()
    current_female = females.popleft()

    if current_female <= 0:
        males.append(current_male)
        continue
    if current_male <= 0:
        females.appendleft(current_female)
        continue

    if current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue
    if current_male % 25 == 0:
        males.pop()
        females.appendleft(current_female)
        continue
    if current_male == current_female:
        matches += 1
    elif current_male != current_female:
        males.append(current_male - 2)

print(f"Matches: {matches}")
if not males:
    print("Males left: none")
else:
    sorted_males = males[::-1]
    print(f"Males left: {', '.join(str(x) for x in sorted_males)}")

if not females:
    print("Females left: none")
else:
    print(f"Females left: {', '.join(str(x) for x in females)}")
