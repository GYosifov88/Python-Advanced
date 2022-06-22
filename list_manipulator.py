def list_manipulator(nums, action, direction, *args):
    args = list(args)
    if action == 'add':
        if direction == 'beginning':
            args.extend(nums)
            nums = args
        elif direction == 'end':
            nums.extend(args)
    if action == 'remove':
        if direction == 'beginning':
            if len(args) == 0:
                nums.pop(0)
            else:
                num_to_be_removed = args.pop()
                del nums[0:num_to_be_removed]
        elif direction == 'end':
            if len(args) == 0:
                nums.pop()
            else:
                num_to_be_removed = args.pop()
                for k in range(num_to_be_removed):
                    nums.pop()
    return nums


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))

