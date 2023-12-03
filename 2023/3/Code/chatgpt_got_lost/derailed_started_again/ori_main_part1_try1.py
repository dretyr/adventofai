def is_adjacent_to_symbol(x, y, schematic):
    symbols = ['*', '#', '+', '$']
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            if 0 <= x + dx < len(schematic) and 0 <= y + dy < len(schematic[x + dx]):
                if schematic[x + dx][y + dy] in symbols:
                    return True
    return False

def sum_part_numbers(file_path):
    with open(file_path, 'r') as file:
        schematic = [line.strip() for line in file]
    
    total_sum = 0
    for i, row in enumerate(schematic):
        num = ''
        for j, char in enumerate(row):
            if char.isdigit():
                num += char
                # Check if it's the last digit in the number
                if j + 1 == len(row) or not row[j + 1].isdigit():
                    if is_adjacent_to_symbol(i, j, schematic):
                        total_sum += int(num)
                    num = ''
            else:
                num = ''
    
    return total_sum

# Example usage
file_path = 'engine_schematic.txt'  # Replace with the path to your engine schematic file
result = sum_part_numbers(file_path)
print("Sum of all part numbers:", result)
