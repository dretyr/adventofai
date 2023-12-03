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



# Find and print gear locations
gear_locations = find_gear_locations(schematic_example)
print(gear_locations)

