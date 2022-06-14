def best_list_pureness(*args):
    nums = args[0]
    rotations = args[1]
    dictionary = {}
    for i in range(rotations + 1):
        sum = 0
        for digit in nums:
            sum += digit * nums.index(digit)
            dictionary[i] = sum
        nums.insert(0, nums.pop())
    max_num = max(dictionary.values())
    max_key = max(dictionary, key=dictionary.get)

    return f"Best pureness {max_num} after {max_key} rotations"


# test = ([4, 3, 2, 6], 4)
# result = best_list_pureness(*test)
# print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

# test = ([1, 2, 3, 4, 5], 10)
# result = best_list_pureness(*test)
# print(result)

