def flights(*args):
    dictionary = {}
    for item1, item2 in zip(args[::2], args[1::2]):
        if item1 == 'Finish':
            break
        if item1 not in dictionary.keys() and item1 != 'Finish':
            dictionary[item1] = item2
        else:
            dictionary[item1] += item2
    return dictionary


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))