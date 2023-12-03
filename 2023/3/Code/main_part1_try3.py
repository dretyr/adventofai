def sum_part_numbers(schematic):
    def is_symbol(char):
        return char not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def adjacent_to_symbol(x, y, grid):
        # Check all adjacent cells including diagonally for a symbol
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and is_symbol(grid[nx][ny]):
                    return True
        return False

    def is_part_of_number_adjacent_to_symbol(number_start_x, number_start_y, number_length, grid):
        # Check each digit of the number for adjacency to a symbol
        for offset in range(number_length):
            if adjacent_to_symbol(number_start_x, number_start_y + offset, grid):
                return True
        return False

    # Convert the schematic into a 2D list
    grid = [list(line) for line in schematic.strip().split('\n')]
    
    total_sum = 0
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            if grid[i][j].isdigit():
                # Start forming the number
                number = grid[i][j]
                start_j = j
                j += 1
                # Continue forming the number while the next characters are digits
                while j < len(grid[i]) and grid[i][j].isdigit():
                    number += grid[i][j]
                    j += 1
                # Check if any part of the number is adjacent to a symbol
                if is_part_of_number_adjacent_to_symbol(i, start_j, len(number), grid):
                    total_sum += int(number)
            else:
                j += 1

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
print(sum_part_numbers(schematic))
