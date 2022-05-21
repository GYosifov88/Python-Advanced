text = input()
characters = {}

for ch in text:
    if ch not in characters:
        characters[ch] = 1
    else:
        characters[ch] += 1


sorted_characters = {key: value for key, value in sorted(characters.items())}
for char in sorted_characters:
    print(f'{char}: {sorted_characters[char]} time/s')
