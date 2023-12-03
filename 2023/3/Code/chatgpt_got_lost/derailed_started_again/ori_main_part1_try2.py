def sum_part_numbers(file_path):
    with open(file_path, 'r') as file:
        schematic = [list(line.strip()) for line in file]

    symbols = ['*', '#', '+', '$']
    total_sum = 0

    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            if schematic[i][j].isdigit():
                # Check if the digit is adjacent to a symbol
                adjacent_to_symbol = False
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        nx, ny = i + dx, j + dy
                        if 0 <= nx < len(schematic) and 0 <= ny < len(schematic[nx]):
                            if schematic[nx][ny] in symbols:
                                adjacent_to_symbol = True
                                break
                    if adjacent_to_symbol:
                        break

                if adjacent_to_symbol:
                    # Extract the full number
                    num = schematic[i][j]
                    k = j + 1
                    while k < len(schematic[i]) and schematic[i][k].isdigit():
                        num += schematic[i][k]
                        k += 1
                    total_sum += int(num)
                    # Skip the digits already processed
                    j = k - 1

    return total_sum

# Example usage
file_path = 'engine_schematic.txt'  # Replace with the path to your engine schematic file
result = sum_part_numbers(file_path)
print("Sum of all part numbers:", result)
