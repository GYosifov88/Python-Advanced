from collections import deque

vowels = deque(input().split())
consonants = input().split()

flowers = {'rose': ['r', 'o', 's', 'e'], 'tulip': ['t', 'u', 'l', 'i', 'p'], 'lotus': ['l', 'o', 't', 'u', 's'],
           'daffodil': ['d', 'a', 'f', 'f', 'o', 'd', 'i', 'l']}
flower_found = False

while vowels and consonants and not flower_found:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for key in flowers.keys():
        if current_vowel in flowers[key]:
            flowers[key] = [x for x in flowers[key] if x != current_vowel]
        if current_consonant in flowers[key]:
            flowers[key] = [x for x in flowers[key] if x != current_consonant]
        if len(flowers[key]) <= 0:
            print(f"Word found: {key}")
            flower_found = True
            break

if not flower_found:
    print("Cannot find any word!")

if len(vowels) > 0:
    print(f"Vowels left: {' '.join(vowels)}")

if len(consonants) > 0:
    print(f"Consonants left: {' '.join(consonants)}")
