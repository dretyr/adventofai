def sum_gear_ratios_debug(schematic):
    def is_gear(char):
        return char == '*'

    def get_adjacent_part_numbers(x, y, grid):
        part_numbers = []
        # Check all adjacent cells including diagonally
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                # Check for multi-digit numbers
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny].isdigit():
                    # Check if this digit is the start of a number
                    # if (ny == 0 or not grid[nx][ny - 1].isdigit()) and (nx == 0 or not grid[nx - 1][ny].isdigit()):
                    number = grid[nx][ny]
                    extend_y = ny + 1
                    # Continue forming the number while the next characters are digits
                    while extend_y < len(grid[0]) and grid[nx][extend_y].isdigit():
                        number += grid[nx][extend_y]
                        extend_y += 1
                    part_numbers.append(int(number))
                    break
        return part_numbers

    # Convert the schematic into a 2D list
    grid = [list(line) for line in schematic.strip().split('\n')]
    
    total_sum = 0
    gear_part_pairs = []  # List to maintain pairs of part numbers adjacent to gears
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_gear(grid[i][j]):
                part_numbers = get_adjacent_part_numbers(i, j, grid)
                if len(part_numbers) == 2:
                    # Calculate the product of the two part numbers
                    total_sum += part_numbers[0] * part_numbers[1]
                    # Add the pair of part numbers to the list
                    gear_part_pairs.append(part_numbers)

    return total_sum, gear_part_pairs

# Running the function with sample data
sum_result, pairs_list = sum_gear_ratios_debug(schematic)
sum_result, pairs_list
print("Sum of Gear Ratios:", sum_result)
print("List of Part Number Pairs Adjacent to Gears:", pairs_list)