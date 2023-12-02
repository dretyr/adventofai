def process_minimum_cubes_from_file(file_path):
    total_power = 0

    with open(file_path, 'r') as file:
        for line in file:
            if not line.strip():
                continue  # Skip empty lines

            _, subsets = line.split(':')
            max_red, max_green, max_blue = 0, 0, 0

            for subset in subsets.split(';'):
                red, green, blue = 0, 0, 0
                for color_info in subset.strip().split(','):
                    number, color = color_info.strip().split()
                    if color == 'red':
                        red = int(number)
                    elif color == 'green':
                        green = int(number)
                    elif color == 'blue':
                        blue = int(number)
                
                max_red = max(max_red, red)
                max_green = max(max_green, green)
                max_blue = max(max_blue, blue)

            game_power = max_red * max_green * max_blue
            total_power += game_power

    return total_power

# Example usage
file_path = 'input.txt'  # Replace 'input.txt' with the path to your input file
result = process_minimum_cubes_from_file(file_path)
print("Sum of the power of the minimum sets:", result)
