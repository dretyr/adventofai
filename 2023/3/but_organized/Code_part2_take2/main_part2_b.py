def find_gear_locations(schematic):
    grid = schematic.split('\n')
    gear_locations = []
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '*':
                gear_locations.append((i, j))
    return gear_locations

def get_adjacent_part_numbers(grid, row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    part_numbers = []

    def read_full_number(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or not grid[i][j].isdigit():
            return ""
        start = j
        while start > 0 and grid[i][start - 1].isdigit():
            start -= 1
        number = ""
        while start < len(grid[0]) and grid[i][start].isdigit():
            number += grid[i][start]
            start += 1
        return number

    for dx, dy in directions:
        new_row, new_col = row + dx, col + dy
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            number = read_full_number(new_row, new_col)
            if number and number not in part_numbers:
                part_numbers.append(number)
    return part_numbers

def sum_gear_ratios(gear_locations_with_parts):
    total_sum = 0
    products = []
    for location in gear_locations_with_parts:
        row, col, part_numbers = location
        if len(part_numbers) == 2:
            num1, num2 = map(int, part_numbers)
            product = num1 * num2
            total_sum += product
            products.append(product)
    return total_sum, products

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
print("Gear locations:", gear_locations)

# Storing gear locations with their adjacent part numbers
gear_locations_with_parts = []
for row, col in gear_locations:
    adjacent_parts = get_adjacent_part_numbers(schematic_example.split('\n'), row, col)
    gear_locations_with_parts.append((row, col, adjacent_parts))

print("\nGear locations with adjacent part numbers:")
for location in gear_locations_with_parts:
    print(f"Gear at row {location[0]}, column {location[1]} with adjacent part numbers: {location[2]}")

# Calculate and print the total sum of gear ratios and individual products
total_gear_ratio_sum, products = sum_gear_ratios(gear_locations_with_parts)
print("\nList of products of adjacent numbers:", products)
print("\nTotal sum of gear ratios:", total_gear_ratio_sum)
