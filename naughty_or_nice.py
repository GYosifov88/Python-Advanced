def naughty_or_nice_list(listing, *args, **kwargs):
    dictionary = {'Nice': [], 'Naughty': [], 'Not found': []}
    digits_count = []
    list_with_names = []
    for k in listing:
        nums = k[0]
        digits_count.append(nums)
    for item in args:
        current = item.split('-')
        num = int(current[0])
        type = current[1]
        for i in listing:
            santa_num = i[0]
            santa_name = i[1]
            if digits_count.count(int(num)) > 1:
                continue
            elif type == 'Naughty' and num == santa_num:
                dictionary['Naughty'].append(santa_name)
                listing.remove(i)
            elif type == 'Nice' and num == santa_num:
                dictionary['Nice'].append(santa_name)
                listing.remove(i)

    for k in listing:
        name = k[1]
        list_with_names.append(name)

    for name, kind in kwargs.items():
        if list_with_names.count(name) > 1:
            continue
        else:
            for j in listing:
                santa_list_name = j[1]
                if name == santa_list_name:
                    if kind == 'Naughty':
                        dictionary['Naughty'].append(name)
                        listing.remove(j)
                    elif kind == 'Nice':
                        dictionary['Nice'].append(name)
                        listing.remove(j)
    if len(listing) > 0:
        for p in listing:
            left_name = p[1]
            dictionary['Not found'].append(left_name)

    final = [f"{type}: {', '.join(names)}" for type, names in dictionary.items() if len(names) > 0]

    return '\n'.join(final)


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))


# print(naughty_or_nice_list(
#     [
#         (7, "Peter"),
#         (1, "Lilly"),
#         (2, "Peter"),
#         (12, "Peter"),
#         (3, "Simon"),
#     ],
#     "3-Nice",
#     "5-Naughty",
#     "2-Nice",
#     "1-Nice",
#     ))
#
#
# print(naughty_or_nice_list(
#     [
#         (6, "John"),
#         (4, "Karen"),
#         (2, "Tim"),
#         (1, "Merry"),
#         (6, "Frank"),
#     ],
#     "6-Nice",
#     "5-Naughty",
#     "4-Nice",
#     "3-Naughty",
#     "2-Nice",
#     "1-Naughty",
#     Frank="Nice",
#     Merry="Nice",
#     John="Naughty",
# ))

