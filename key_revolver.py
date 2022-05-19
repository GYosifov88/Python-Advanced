from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split(' ')]
locks = deque([int(x) for x in input().split(' ')])
intelligence_value = int(input())
current_barrel = 0
bullets_shot = 0
while True:
    if len(locks) == 0:
        money_earned = intelligence_value - bullets_shot * bullet_price
        print(f"{len(bullets)} bullets left. Earned ${money_earned}")
        break
    elif len(bullets) == 0:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
    elif len(locks) > 0 and len(bullets) > 0:
        if bullets[-1] > locks[0]:
            print('Ping!')
            bullets.pop()
            current_barrel += 1
            bullets_shot += 1
            if current_barrel == gun_barrel_size:
                if len(bullets) > 0:
                    print('Reloading!')
                    current_barrel = 0
                    continue
        elif bullets[-1] <= locks[0]:
            print('Bang!')
            bullets.pop()
            locks.popleft()
            current_barrel += 1
            bullets_shot += 1
            if current_barrel == gun_barrel_size:
                if len(bullets) > 0:
                    print('Reloading!')
                    current_barrel = 0
                    continue
