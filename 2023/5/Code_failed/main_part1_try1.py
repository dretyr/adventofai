def parse_map(map_str):
    """ Parses a conversion map from a string into a dictionary. """
    conversion_map = {}
    for line in map_str.split('\n'):
        if line.strip():
            dest_start, src_start, length = map(int, line.split())
            for i in range(length):
                conversion_map[src_start + i] = dest_start + i
    return conversion_map

def convert_number(number, conversion_map):
    """ Converts a number using the given conversion map. """
    return conversion_map.get(number, number)

def process_seed(seed, maps):
    """ Processes a seed through all the maps to find its final location number. """
    for map_name in ['soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']:
        seed = convert_number(seed, maps[map_name])
    return seed

def find_lowest_location(seeds, maps):
    """ Finds the lowest location number for the given seeds. """
    location_numbers = [process_seed(seed, maps) for seed in seeds]
    return min(location_numbers)

# Example usage (you'll need to replace the following example data with the actual data from your input file)
example_data = """
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

# Parsing the example data
data_sections = example_data.split('\n\n')
seeds = list(map(int, data_sections[0].split(':')[1].split()))

maps = {}
for section in data_sections[1:]:
    map_name, map_str = section.split(' map:\n')
    maps[map_name.strip()] = parse_map(map_str)

# Find the lowest location number
lowest_location = find_lowest_location(seeds, maps)
print(lowest_location)
