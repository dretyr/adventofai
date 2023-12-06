def read_almanac_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_map(map_str):
    ranges = []
    for line in map_str.split('\n'):
        if line.strip():
            dest_start, src_start, length = map(int, line.split())
            ranges.append((src_start, src_start + length, dest_start))
    return ranges

def convert_range(start, length, ranges, memo):
    # If the range is already computed, return the result
    if (start, length) in memo:
        return memo[(start, length)]

    converted_range = []
    for i in range(start, start + length):
        for src_start, src_end, dest_start in ranges:
            if src_start <= i < src_end:
                converted_range.append(i - src_start + dest_start)
                break
        else:
            converted_range.append(i)

    memo[(start, length)] = converted_range
    return converted_range

def process_seed_range(start, length, maps, memos):
    for map_name in maps:
        print(f"start = {map_name}")
        start, length = min(convert_range(start, length, maps[map_name], memos[map_name])), length
        print("...done")
    return start

def find_lowest_location(seed_ranges, maps):
    memos = {map_name: {} for map_name in maps}
    lowest_location = float('inf')
    for start, length in seed_ranges:
        print(f"start = {start}, length = {length}")
        lowest_location_in_range = process_seed_range(start, length, maps, memos)
        lowest_location = min(lowest_location, lowest_location_in_range)
    return lowest_location

# Function to parse the entire almanac data including seed ranges
def parse_almanac(almanac_data):
    data_sections = almanac_data.split('\n\n')
    seed_ranges = [(int(x), int(y)) for x, y in zip(data_sections[0].split(':')[1].split()[::2], data_sections[0].split(':')[1].split()[1::2])]

    maps = {}
    for section in data_sections[1:]:
        map_name, map_str = section.split(' map:\n')
        maps[map_name.strip()] = parse_map(map_str)
    
    return seed_ranges, maps

# Example usage
file_path = 'almanac.txt'  # Replace with the actual file path
almanac_data = read_almanac_from_file(file_path)
seed_ranges, maps = parse_almanac(almanac_data)
lowest_location = find_lowest_location(seed_ranges, maps)
print(lowest_location)
