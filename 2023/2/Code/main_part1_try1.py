def is_game_possible(game_details, red_cubes, green_cubes, blue_cubes):
    for subset in game_details:
        if subset['red'] > red_cubes or subset['green'] > green_cubes or subset['blue'] > blue_cubes:
            return False
    return True

def process_games(input_data):
    games = input_data.split('\n')
    possible_games_sum = 0

    for game in games:
        game_id, subsets = game.split(':')
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
input_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

result = process_games(input_data)
print("Sum of IDs of possible games:", result)

