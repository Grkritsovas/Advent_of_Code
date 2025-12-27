# Part 1
sum_of_invalid_ids = 0
with open ('input.txt', 'r') as content_file:
    content = content_file.read()

id_ranges = content.split(',')

for id_range in id_ranges:
    start, end = map(int, id_range.split('-'))
    if len(str(start)) % 2 != 0:
        if len(str(end)) > len(str(start)):
            start = int('1' + '0' * len(str(start)))
    if len(str(end)) % 2 != 0:
        if len(str(end)) > len(str(start)):
            end = int('9' * (len(str(end))-1))
    for item_id in range(start, end + 1):
        string_id = str(item_id)
        mid = len(string_id) // 2
        left_half, right_half = string_id[:mid], string_id[mid:]

        if left_half == right_half:
            sum_of_invalid_ids += item_id

print('Sum of invalid item IDs: ', sum_of_invalid_ids)

# Part 2
sum_of_invalid_ids_part_2 = 0

def is_repeated_pattern(item_id: int) -> bool:
    string_id = str(item_id)
    string_size = len(string_id)
    for index in range(1, string_size // 2 + 1):
        # only consider index (pattern lengths) that divide the full length exactly
        if string_size % index != 0:
            continue
        pattern = string_id[:index]
        # check if repeating the pattern forms the original string
        if pattern * (string_size // index) == string_id:
            return True
    return False

for id_range in id_ranges:
    start, end = map(int, id_range.split('-'))

    for item_id in range(start, end + 1):
        if is_repeated_pattern(item_id):
            sum_of_invalid_ids_part_2 += item_id

print('Sum of invalid item IDs: ', sum_of_invalid_ids_part_2)