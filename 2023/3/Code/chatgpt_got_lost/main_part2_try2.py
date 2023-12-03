def sum_gear_ratios(schematic):
    def is_digit_or_empty(char):
        return char.isdigit() or char == '.'

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
                    number = grid[nx][ny]
                    ny += 1
                    # Continue forming the number while the next characters are digits
                    while ny < len(grid[0]) and grid[nx][ny].isdigit():
                        number += grid[nx][ny]
                        ny += 1
                    part_numbers.append(int(number))
                    break  # Move to the next adjacent cell
        return part_numbers

    # Convert the schematic into a 2D list
    grid = [list(line) for line in schematic.strip().split('\n')]
    
    total_sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if is_gear(grid[i][j]):
                part_numbers = get_adjacent_part_numbers(i, j, grid)
                if len(part_numbers) == 2:
                    # Calculate the product of the two part numbers
                    total_sum += part_numbers[0] * part_numbers[1]
    return total_sum

# Example schematic
## Editor: added this from the first script - ChatGPT must be using a notebook where it doesn't need to add the data again.
schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

# Run the updated function with the example schematic
## Editor: added print - ChatGPT must be checking the value external to the script writing.
print(sum_gear_ratios(schematic))
