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
    # Sort the ranges for efficient processing
    return sorted((src_start, src_end, dest_start) for src_start, src_end, dest_start in ranges)

def find_segment_end(start, end, mappings):
    # Find the nearest end point of a mapping segment
    segment_end = end
    for src_start, src_end, _ in mappings:
        if src_start > start and src_start < segment_end:
            segment_end = src_start
        elif src_end > start and src_end < segment_end:
            segment_end = src_end
    return segment_end

def transform_range(start, length, mappings):
    end = start + length
    transformed_values = []

    i = start
    while i < end:
        segment_end = end
        transformed = i  # Default transformation if no mapping applies
        for src_start, src_end, dest_start in mappings:
            if src_start <= i < src_end:
                # Transform the current number based on the mapping
                offset = i - src_start
                transformed = dest_start + offset
                # Adjust segment end based on the mapping
                segment_end = min(segment_end, src_end)
                break
        transformed_values.append(transformed)
        i = segment_end  # Move to the end of the current segment

    # Return the minimum value from the transformed range
    return min(transformed_values)

def process_seed_range(start, length, maps):
    for map_name in maps:
        mappings = maps[map_name]
        start = transform_range(start, length, mappings)
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
        print("sadf")
        maps[map_name.strip()] = preprocess_mappings(ranges)
        print("::::")    
    return seed_ranges, maps

# Example usage
file_path = 'almanac.txt'  # Replace with the actual file path
almanac_data = read_almanac_from_file(file_path)
seed_ranges, maps = parse_almanac(almanac_data)
lowest_location = find_lowest_location(seed_ranges, maps)
print(lowest_location)
