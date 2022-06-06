def words_sorting(*args):
    dictionary = {}
    total_sum = 0
    for word in args:
        ascii_sum = 0
        for ch in word:
            ascii_sum += ord(ch)
        dictionary[word] = ascii_sum

    total_sum = sum(dictionary.values())

    if total_sum % 2 != 0:
        sorted_dict = [f'{key} - {value}' for key, value in sorted(dictionary.items(), key=lambda x: -x[1])]
    else:
        sorted_dict = [f'{key} - {value}' for key, value in sorted(dictionary.items(), key=lambda x: x[0])]

    return '\n'.join(sorted_dict)



print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

