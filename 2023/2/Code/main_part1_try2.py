def is_game_possible(game_details, red_cubes, green_cubes, blue_cubes):
    for subset in game_details:
        if subset['red'] > red_cubes or subset['green'] > green_cubes or subset['blue'] > blue_cubes:
            return False
    return True

def process_games_from_file(file_path):
    possible_games_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue  # Skip empty lines

            game_id, subsets = line.split(':')
            game_id = int(game_id.replace('Game', '').strip())
            subset_details = subsets.split(';')
            game_details = []

            for subset in subset_details:
                details = {'red': 0, 'green': 0, 'blue': 0}
                for color_info in subset.strip().split(','):
                    number, color = color_info.strip().split()
                    details[color] = int(number)
                game_details.append(details)

            if is_game_possible(game_details, 12, 13, 14):
                possible_games_sum += game_id

    return possible_games_sum

# Example usage
file_path = 'input.txt'  # Replace 'input.txt' with the path to your input file
result = process_games_from_file(file_path)
print("Sum of IDs of possible games:", result)
