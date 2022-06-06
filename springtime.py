def start_spring(**kwargs):
    dictionary = {}
    list_of = []
    for key, value in kwargs.items():
        if value not in dictionary.keys():
            dictionary[value] = []
            dictionary[value].append(key)
        else:
            dictionary[value].append(key)
    for key in dictionary.keys():
        dictionary[key] = sorted(dictionary[key])
    sorted_dict = dict(sorted(dictionary.items(), key=lambda x: (-len(x[1]), x[0])))

    result = []
    for key, value in sorted_dict.items():
        result.append(f"{key}:")
        for el in sorted(value):
            result.append(f"-{el}")

    return "\n".join(result)

example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}

print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))
#
# example_objects = {"Magnolia": "tree",
#                    "Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Pear": "tree",
#                    "Cherries": "tree",
#                    "Shrikes": "bird",
#                    "Butterfly": "insect"}
# print(start_spring(**example_objects))
