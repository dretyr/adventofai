def read_almanac_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_almanac(data):
    sections = data.split('\n\n')
    seed_ranges_raw = [int(x) for x in sections[0].split(': ')[1].split()]
    
    seed_ranges = [(seed_ranges_raw[i], seed_ranges_raw[i] + seed_ranges_raw[i + 1]) for i in range(0, len(seed_ranges_raw), 2)]
    seed_ranges.sort()

    maps = {}
    for section in sections[1:]:
        title, *lines = section.split('\n')
        category = title.split('-to-')[0]
        map_data = [tuple(map(int, line.split())) for line in lines]
        map_data.sort(key=lambda x: x[1])  # Sort by source start value
        maps[category] = map_data
    
    return seed_ranges, maps

def map_value(range_start, range_end, category_map):
    result_ranges = []

    for dest_start, src_start, length in category_map:
        src_end = src_start + length if length > 0 else float('inf')

        # Check for overlap with the current map range
        if src_end > range_start and src_start < range_end:
            mapped_start = max(range_start, src_start)
            mapped_end = min(range_end, src_end)

            # Adjust the mapped range to the destination
            offset = mapped_start - src_start
            mapped_start = dest_start + offset
            mapped_end = dest_start + (mapped_end - src_start)

            result_ranges.append((mapped_start, mapped_end))

    return result_ranges if result_ranges else [(range_start, range_end)]

def process_seed(seed_range, maps):
    categories = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    current_ranges = [seed_range]

    for category in categories:
        next_ranges = []
        for r_start, r_end in current_ranges:
            mapped_ranges = map_value(r_start, r_end, maps.get(category, []))
            next_ranges.extend(mapped_ranges)
        current_ranges = next_ranges

    return current_ranges

def complete_maps(maps):
    completed_maps = {}
    for category, map_data in maps.items():
        if not map_data:
            completed_maps[category] = [(0, 0, 0)]  # If map is empty, cover the entire range with itself
            continue

        # Sort the map data by source start value
        map_data.sort(key=lambda x: x[1])
        completed_map = []

        # Add an initial range if necessary
        if map_data[0][1] > 0:
            completed_map.append((0, 0, map_data[0][1]))

        # Fill gaps between existing ranges
        for i in range(len(map_data)):
            completed_map.append(map_data[i])
            if i < len(map_data) - 1 and map_data[i][1] + map_data[i][2] < map_data[i + 1][1]:
                gap_start = map_data[i][1] + map_data[i][2]
                gap_end = map_data[i + 1][1]
                completed_map.append((gap_start, gap_start, gap_end - gap_start))

        # Add a final range if necessary
        last_range_end = map_data[-1][1] + map_data[-1][2]
        completed_map.append((last_range_end, last_range_end, 0))  # 0 in the length field to denote all numbers greater

        completed_maps[category] = completed_map
    
    return completed_maps

# Read data from 'almanac.txt'
almanac_data = read_almanac_from_file('almanac.txt')
almanac_data = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
seed_ranges, maps = parse_almanac(almanac_data.strip())
completed_maps = complete_maps(maps)

print("Seed ranges:", seed_ranges)
for category, map_data in completed_maps.items():
    print(f"{category}-to map completed:", map_data)

# Process each seed range through the maps
for seed_range in seed_ranges:
    final_ranges = process_seed(seed_range, completed_maps)
    print(f"Final ranges for seed {seed_range}: {final_ranges}")

# To find the lowest value, we can do:
lowest_value = min([r[0] for final_range in final_ranges for r in final_range], default=None)
print("Lowest value:", lowest_value)
