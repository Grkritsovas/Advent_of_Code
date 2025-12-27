times_landed_to_zero = 0
position = 50
# Part 1
with open('input.txt', 'r') as file:
    for line in file:
        direction = line[0]
        amount = int(line[1:].strip()) % 100 # Wrap around at 100

        # only final position matters; wrap amount to 0–99
        steps = amount % 100

        if direction == 'R':
            position = (position + steps) % 100
        else:
            position = (position - steps) % 100

        if position == 0:
            times_landed_to_zero += 1

print('Times rotation landed to zero: ', times_landed_to_zero)

# Part 2
times_crossed_zero = 0
with open('input.txt', 'r') as file:
    position = 50
    for line in file:
        direction = line[0]
        amount = int(line[1:].strip())
        # count how many times this move hits 0
        if direction == 'R':
            # first time we'd hit 0 going right
            first = (100 - position) % 100
            if first == 0:
                first = 100
        else:
            # first time we’d hit 0 going left
            first = position % 100
            if first == 0:
                first = 100

        if amount >= first:
            times_crossed_zero += 1 + (amount - first) // 100

        # move the dial
        if direction == 'R':
            position = (position + amount) % 100
        else:
            position = (position - amount) % 100

print('Total times crossed from zero: ', times_crossed_zero)