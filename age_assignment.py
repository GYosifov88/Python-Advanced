def age_assignment(*args, **kwargs):
    people = []
    result = {}
    some_list = []
    for person in args:
        people.append(person)

    for key, value in kwargs.items():
        for ind in people:
            if key == ind[0]:
                result[ind] = value

    result = dict(sorted(result.items()))
    for k in result:
        some_list.append(f"{k} is {result[k]} years old.")
    return '\n'.join(some_list)

print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))