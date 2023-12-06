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

def convert_range(start, length, ranges):
    converted_range = []
    for i in range(start, start + length):
        for src_start, src_end, dest_start in ranges:
            if src_start <= i < src_end:
                converted_range.append(i - src_start + dest_start)
                break
        else:
            converted_range.append(i)
    return converted_range

def process_seed_range(start, length, maps):
    seed_range = range(start, start + length)
    for map_name in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
        seed_range = convert_range(start, length, maps[map_name])
        start = seed_range[0]
        length = len(seed_range)
    return seed_range

def find_lowest_location(seed_ranges, maps):
    lowest_location = float('inf')  # Initialize with infinity
    for start, length in seed_ranges:
        print(f"start = {start}, length = {length}")
        processed_range = process_seed_range(start, length, maps)
        min_location_in_range = min(processed_range)
        lowest_location = min(lowest_location, min_location_in_range)
    return lowest_location

# Function to parse the entire almanac data including seed ranges
def parse_almanac(almanac_data):
    data_sections = almanac_data.split('\n\n')
    print("pre-zip")
    seed_ranges = [(int(x), int(y)) for x, y in zip(data_sections[0].split(':')[1].split()[::2], data_sections[0].split(':')[1].split()[1::2])]

    maps = {}
    for section in data_sections[1:]:
        map_name, map_str = section.split(' map:\n')
        print(f"Parsing stuff: {map_name.strip()}")
        maps[map_name.strip()] = parse_map(map_str)
    
    return seed_ranges, maps

# Example usage
file_path = 'almanac.txt'  # Replace with the actual file path
almanac_data = read_almanac_from_file(file_path)
seed_ranges, maps = parse_almanac(almanac_data)
print("done with map")
lowest_location = find_lowest_location(seed_ranges, maps)
print(lowest_location)
