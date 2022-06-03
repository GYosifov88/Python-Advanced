def even_odd_filter(**kwargs):
    dictionary = {}
    for key, value in kwargs.items():
        if key == 'even':
            dictionary[key] = []
            for el in value:
                if el % 2 == 0:
                    dictionary[key].append(el)
        if key == 'odd':
            dictionary[key] = []
            for el in value:
                if el % 2 != 0:
                    dictionary[key].append(el)
    sorted_list = dict(sorted(dictionary.items(), key=lambda x: -len(x[1])))
    return sorted_list


print(even_odd_filter(
        odd=[1, 2, 3, 4, 10, 5],
        even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
    ))
print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))


