def find_gear_locations(schematic):
    def is_gear(char):
        return char == '*'

    # Convert the schematic into a 2D list
    grid = [list(line) for line in schematic.strip().split('\n')]

    # Find and return all gear locations
    gear_locations = [(i, j) for i in range(len(grid)) for j in range(len(grid[i])) if is_gear(grid[i][j])]
    return gear_locations

# Sample schematic
sample_schematic = """
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

# Find gear locations in the sample schematic
gear_locations = find_gear_locations(sample_schematic)
print(gear_locations)

