def parse_almanac(data):
    sections = data.split('\n\n')
    seeds = [int(x) for x in sections[0].split(': ')[1].split()]
    
    maps = {}
    for section in sections[1:]:
        title, *lines = section.split('\n')
        category = title.split('-to-')[0]
        maps[category] = [tuple(map(int, line.split())) for line in lines]
    
    return seeds, maps

def map_value(value, category_map):
    for dest_start, src_start, length in category_map:
        if src_start <= value < src_start + length:
            return dest_start + (value - src_start)
    return value

def process_seed(seed, maps):
    categories = ["seed", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    value = seed
    for category in categories:
        value = map_value(value, maps.get(category, []))
    return value

# Example data (later this will be replaced with file reading)
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

seeds, maps = parse_almanac(example_data.strip())
locations = [process_seed(seed, maps) for seed in seeds]
lowest_location = min(locations)

print("Lowest location number:", lowest_location)
