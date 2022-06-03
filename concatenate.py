def concatenate(*args, **kwargs):
    word = ''
    for el in args:
        word += el
    # word = ''.join(args)
    for key, value in kwargs.items():
        word = word.replace(key, value)
    return word

print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))

print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))