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

def preprocess_mappings(ranges):
    max_num = max(src_end for _, src_end, _ in ranges)
    lookup = list(range(max_num))

    for src_start, src_end, dest_start in ranges:
        for i in range(src_start, src_end):
            lookup[i] = dest_start + (i - src_start)

    return lookup

def convert_range(start, length, lookup):
    converted_values = lookup[start:start + length]
    return min(converted_values)

def process_seed_range(start, length, maps):
    for map_name in maps:
        lookup = maps[map_name]
        start = convert_range(start, length, lookup)
    return start

def find_lowest_location(seed_ranges, maps):
    lowest_location = float('inf')
    for start, length in seed_ranges:
        lowest_location_in_range = process_seed_range(start, length, maps)
        lowest_location = min(lowest_location, lowest_location_in_range)
    return lowest_location

# Function to parse the entire almanac data including seed ranges
def parse_almanac(almanac_data):
    data_sections = almanac_data.split('\n\n')
    seed_ranges = [(int(x), int(y)) for x, y in zip(data_sections[0].split(':')[1].split()[::2], data_sections[0].split(':')[1].split()[1::2])]

    maps = {}
    for section in data_sections[1:]:
        map_name, map_str = section.split(' map:\n')
        ranges = parse_map(map_str)
        maps[map_name.strip()] = preprocess_mappings(ranges)
    
    return seed_ranges, maps

# Example usage
file_path = 'example_data.txt'  # Replace with the actual file path
almanac_data = read_almanac_from_file(file_path)
seed_ranges, maps = parse_almanac(almanac_data)
lowest_location = find_lowest_location(seed_ranges, maps)
print(lowest_location)
