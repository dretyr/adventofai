def find_gear_locations(schematic):
    # Split the schematic into lines to create a 2D grid
    grid = schematic.split('\n')
    
    # List to store the locations of gears
    gear_locations = []

    # Iterate over the grid to find gears
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '*':  # Identifying a gear
                gear_locations.append((i, j))

    return gear_locations

def get_adjacent_part_numbers(grid, row, col):
    # Directions to check around the gear (8 directions)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    # Store the adjacent part numbers
    part_numbers = []

    # Function to read a full number starting from a digit
    def read_full_number(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or not grid[i][j].isdigit():
            return ""
        # Move left in the row to find the start of the number
        start = j
        while start > 0 and grid[i][start - 1].isdigit():
            start -= 1
        # Read the full number from start to the right
        number = ""
        while start < len(grid[0]) and grid[i][start].isdigit():
            number += grid[i][start]
            start += 1
        return number

    # Check adjacent cells for part numbers
    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            number = read_full_number(new_row, new_col)
            if number and number not in part_numbers:
                part_numbers.append(number)

    return part_numbers

# Example engine schematic
schematic_example = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

# Find gear locations
gear_locations = find_gear_locations(schematic_example)

# Storing gear locations with their adjacent part numbers
gear_locations_with_parts = []

for row, col in gear_locations:
    adjacent_parts = get_adjacent_part_numbers(schematic_example.split('\n'), row, col)
    if adjacent_parts:
        gear_locations_with_parts.append((row, col, adjacent_parts))

# Output
for location in gear_locations_with_parts:
    print(f"Gear at row {location[0]}, column {location[1]} with adjacent part numbers: {location[2]}")
