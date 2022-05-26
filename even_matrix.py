rows = int(input())
result = []

for _ in range(rows):
    row = [int(x) for x in input().split(', ')]
    result.append(
        [x for x in row if x % 2 == 0]
    )

print(result)




# rows = int(input())
#
# major = []
#
# for _ in range(rows):
#     inside = []
#     digits = [int(x) for x in input().split(', ')]
#     for x in digits:
#         if x % 2 == 0:
#             inside.append(x)
#     major.append(inside)
# print(major)