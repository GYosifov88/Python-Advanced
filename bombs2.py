from collections import deque

bomb_effect = deque(int(x) for x in input().split(', '))
bomb_casing = [int(x) for x in input().split(', ')]

cherry_bombs = 0
datura_bombs = 0
smoke_decoy_bombs = 0
all_bomb_collected = False
while bomb_effect and bomb_casing:
    current_bomb = int(bomb_effect[0])
    current_casing = int(bomb_casing[-1])
    sum = current_casing + current_bomb
    if sum == 40:
        datura_bombs += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    elif sum == 60:
        cherry_bombs += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    elif sum == 120:
        smoke_decoy_bombs += 1
        bomb_effect.popleft()
        bomb_casing.pop()
    else:
        bomb_casing[-1] -= 5

    if cherry_bombs >= 3 and datura_bombs >= 3 and smoke_decoy_bombs >= 3:
        all_bomb_collected = True
        break

if all_bomb_collected:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join(str(x) for x in bomb_effect)}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join(str(x) for x in bomb_casing)}")
else:
    print("Bomb Casings: empty")

print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")

