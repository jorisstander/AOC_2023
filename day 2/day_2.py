power = 0
result = 0
with open("puzzle_data.txt") as file:
    for line in file:

        bag = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        # replace \n
        line = line.replace("\n", "")

        game_split = line.split(':')
        game = game_split[0].split()

        game_id = game[1]
        set_info = game_split[1].split(';')
        valid_sets = []

        for combo in set_info:
            combo = combo.split(',')
            for current_combo in combo:
                current_combo = current_combo.split()
                amount = current_combo[0]
                colour = current_combo[1]
                if int(amount) > int(bag[colour]):
                    bag[colour] = amount

        power = int(bag['green']) * int(bag['blue']) * int(bag['red'])
        result += power

    print(result)