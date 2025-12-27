# Part 1
total_output_joltage = 0
with open ('input.txt', 'r') as content_file:
    for line in content_file:
        line = line.strip()
        # find highest joltage and its index
        highest_joltage = max(line)
        first_index = line.index(highest_joltage)
        # If: highest digit is the last character, can't be the beginning of the subsequence
        # find second highest in the rest of the line to use it as the first digit instead
        if first_index == len(line) - 1:
            second_highest_joltage = max(line[:first_index])

            curr_highest_joltage_combination = int(second_highest_joltage + highest_joltage)
            total_output_joltage += curr_highest_joltage_combination
            continue

        # else find second highest joltage after the first highest
        second_highest_joltage = max(line[first_index + 1:])
        curr_highest_joltage_combination = int(highest_joltage + second_highest_joltage)
        
        total_output_joltage += curr_highest_joltage_combination

print('Total output joltage: ', total_output_joltage)

# Part 2
total_output_joltage_2 = 0
with open ('input.txt', 'r') as content_file:
    for line in content_file:
        line = line.strip()
        # dictionary mapping Index -> Joltage Value
        position_joltage_map = {}
        for i, joltage_value in enumerate(line):
            position_joltage_map[i] = joltage_value

        curr_highest_joltage_combination = ''
        curr_available_spots = 12
        # we need to pick 12 numbers
        for _ in range(12):
            # Sort Strategy | Primary: Joltage Value Descending (x[1]) - 9s before 8s | Secondary: Index Ascending (-x[0])
            # If we have two 9s, pick the earliest one to leave maximum room for future digits.
            for index, joltage_value in sorted(position_joltage_map.items(), key=lambda x: (x[1], -x[0]), reverse = True):
                # Check if picking this digit leaves enough room for the remaining needed spots
                if index + curr_available_spots <= len(line):
                    curr_highest_joltage_combination += joltage_value
                    curr_available_spots -= 1
                    # Remove this index and all previous indices from the map.
                    # We cannot go backwards, so everything before this index is now invalid.
                    for i in range(index+1):
                        position_joltage_map.pop(i, None)
                    # Break to restart the search for the next digit using the updated map
                    break
        total_output_joltage_2 += int(curr_highest_joltage_combination)

print('Total output joltage: ', total_output_joltage_2)