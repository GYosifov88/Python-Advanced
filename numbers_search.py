def numbers_searching(*args):
    final_list = []
    duplicates = []

    args = sorted(args)
    start = args[0]
    end = args[-1]
    missing_num = sorted(set(range(start, end + 1)).difference(args))
    final_list.append(missing_num[0])

    for num in args:
        if args.count(num) > 1:
            if num not in duplicates:
                duplicates.append(num)
    final_list.append(sorted(duplicates))
    return final_list


print(numbers_searching(1, 2, 4, 2, 5, 4))

print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))