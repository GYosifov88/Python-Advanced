def read_matrix():
    rows, columns = [int(x) for x in input().split(', ')]
    major = []
    for _ in range(rows):
        digits = [int(x) for x in input().split(', ')]
        major.append(digits)
    return major

major = read_matrix()
whole_total = 0

for k in major:
    for l in k:
        whole_total += l

print(whole_total)
print(major)
