number_of_lines = int(input())

intersections_list = []
longest = {}
for i in range(number_of_lines):
    first_list = set()
    second_list = set()
    intersection = set()
    current_brackets = input().split('-')
    first_bracket = current_brackets[0].split(',')
    first_start = int(first_bracket[0])
    first_end = int(first_bracket[1])
    second_bracket = current_brackets[1].split(',')
    second_start = int(second_bracket[0])
    second_end = int(second_bracket[1])
    for k in range(first_start, first_end+1):
        first_list.add(k)
    for j in range(second_start, second_end+1):
        second_list.add(j)
    intersection = first_list & second_list
    intersections_list.append(intersection)

longest_list = max(len(elem) for elem in intersections_list)
longest_el_list = max(intersections_list, key=len)
final_longest_list = map(str, longest_el_list)

print(f"Longest intersection is [{', '.join(final_longest_list)}] with length {longest_list}")