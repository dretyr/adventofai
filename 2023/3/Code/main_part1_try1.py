def sum_part_numbers(schematic):
    def is_symbol(char):
        return char not in ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    def adjacent_to_symbol(x, y, grid):
        # Check all adjacent cells including diagonally
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and is_symbol(grid[nx][ny]):
                    return True
        return False

    # Convert the schematic into a 2D list
    grid = [list(line) for line in schematic.strip().split('\n')]
    
    total_sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].isdigit() and adjacent_to_symbol(i, j, grid):
                total_sum += int(grid[i][j])

    return total_sum

# Example schematic
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

print(sum_part_numbers(schematic))
