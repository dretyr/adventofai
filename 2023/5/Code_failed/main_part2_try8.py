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

# def convert_range(start, length, ranges, memo):
#     # Create a unique key for memoization
#     range_key = (start, length)
#     if range_key in memo:
#         return memo[range_key]

#     end = start + length
#     converted_start = start
#     i = start

#     while i < end:
#         # Check if this individual number conversion is already memoized
#         if i in memo:
#             i += 1
#             continue

#         for src_start, src_end, dest_start in ranges:
#             if src_start <= i < src_end:
#                 # Calculate offset and map the range
#                 offset = i - src_start
#                 new_start = dest_start + offset
#                 converted_start = min(converted_start, new_start)
                
#                 # Move i to the end of this mapping segment
#                 i = min(end, src_end)
#                 break
#         else:
#             i += 1  # No mapping found, move to the next number

#     memo[range_key] = converted_start
#     return converted_start

# def convert_range(start, length, ranges, memo):
#     # Check if the range conversion is already memoized
#     range_key = (start, length)
#     if range_key in memo:
#         return memo[range_key]

#     end = start + length
#     converted_values = []

#     for i in range(start, end):
#         print(i)
#         # Check if the individual number conversion is already memoized
#         if i in memo:
#             converted_values.append(memo[i])
#             continue

#         converted_number = i  # Default if no mapping is found
#         for src_start, src_end, dest_start in ranges:
#             if src_start <= i < src_end:
#                 # Convert the number based on the current mapping
#                 converted_number = dest_start + (i - src_start)
#                 break

#         # Memoize the converted number
#         memo[i] = converted_number
#         converted_values.append(converted_number)

#     # Find the minimum value in the converted range as the representative
#     min_converted_value = min(converted_values)
#     memo[range_key] = min_converted_value
#     return min_converted_value

def convert_range(start, length, ranges, memo):
    # Check if the range conversion is already memoized
    range_key = (start, length)
    if range_key in memo:
        return memo[range_key]

    end = start + length
    min_converted_value = float('inf')

    i = start
    while i < end:
        # If individual number conversion is memoized, use it
        if i in memo:
            min_converted_value = min(min_converted_value, memo[i])
            i += 1
            continue

        for src_start, src_end, dest_start in ranges:
            if src_start <= i < src_end:
                offset = i - src_start
                new_start = dest_start + offset
                new_end = min(end, src_end - offset + dest_start)

                # Convert the segment and update the minimum value
                for j in range(new_start, new_end):
                    memo[j] = j
                    min_converted_value = min(min_converted_value, j)

                # Advance i to the end of the segment
                i = src_end - offset + dest_start
                break
        else:
            # No mapping found, use the number as is
            memo[i] = i
            min_converted_value = min(min_converted_value, i)
            i += 1

    memo[range_key] = min_converted_value
    return min_converted_value


def process_seed_range(start, length, maps, memos):
    for map_name in maps:
        print(f"start = {map_name}")
        memo = memos[map_name]
        start = convert_range(start, length, maps[map_name], memo)
        print("...done")
    return start

def find_lowest_location(seed_ranges, maps, memos):
    lowest_location = float('inf')
    for start, length in seed_ranges:
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
file_path = 'example_data.txt'  # Replace with the actual file path
almanac_data = read_almanac_from_file(file_path)
seed_ranges, maps = parse_almanac(almanac_data)
memos = {map_name: {} for map_name in maps}
lowest_location = find_lowest_location(seed_ranges, maps, memos)
print(lowest_location)