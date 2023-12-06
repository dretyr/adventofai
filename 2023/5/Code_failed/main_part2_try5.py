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

# def convert_range(start, length, ranges):
#     dest_start = start
#     for i in range(length):
#         print(i)
#         number = start + i
#         for src_start, src_end, dest_src_start in ranges:
#             if src_start <= number < src_end:
#                 offset = number - src_start
#                 dest_start = min(dest_start, dest_src_start + offset)
#                 break
#         else:
#             dest_start = min(dest_start, number)
#     return dest_start

# def convert_range(start, length, ranges):
#     for src_start, src_end, dest_start in ranges:
#         if src_start <= start < src_end:
#             # Calculate the offset for the start of the range
#             offset = start - src_start
#             # Apply the offset to the destination start
#             return dest_start + offset
#     # If no mapping is found, return the original start
#     return start
def convert_range(start, length, ranges):
    for src_start, src_end, dest_start in ranges:
        if src_start <= start < src_end:
            # Calculate the offset for the start of the range
            offset = start - src_start
            # Apply the offset to the destination start
            new_start = dest_start + offset

            # Check if the entire range fits in the destination range
            if new_start + length <= dest_start + (src_end - src_start):
                return new_start
            else:
                # Handle cases where the range spans multiple mappings
                return min([convert_individual_number(start + i, ranges) for i in range(length)])

    # If no mapping is found, return the original start
    return start

def convert_individual_number(number, ranges):
    for src_start, src_end, dest_start in ranges:
        if src_start <= number < src_end:
            return number - src_start + dest_start
    return number


def process_seed_range(start, length, maps):
    for map_name in maps:
        print(f"start = {map_name}")
        start = convert_range(start, length, maps[map_name])
        print("...done")
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
        maps[map_name.strip()] = parse_map(map_str)
    
    return seed_ranges, maps

# Example usage
file_path = 'almanac.txt'  # Replace with the actual file path
almanac_data = read_almanac_from_file(file_path)
seed_ranges, maps = parse_almanac(almanac_data)
lowest_location = find_lowest_location(seed_ranges, maps)
print(lowest_location)