number = 0
puzzle_1 = 0
puzzle_2 = 0
with open("puzzle_data.txt") as file:
    for line in file:
        p1_digits = []
        p2_digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                p1_digits.append(c)
                p2_digits.append(c)
            for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
                if line[i:].startswith(val):
                    p2_digits.append(str(d + 1))
        puzzle_1 += int(p1_digits[0] + p1_digits[-1])
        puzzle_2 += int(p2_digits[0] + p2_digits[-1])
    print(puzzle_1)
    print(puzzle_2)
