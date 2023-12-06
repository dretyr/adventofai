def read_almanac_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

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

# Read data from 'almanac.txt'
almanac_data = read_almanac_from_file('almanac.txt')

seeds, maps = parse_almanac(almanac_data.strip())
locations = [process_seed(seed, maps) for seed in seeds]
lowest_location = min(locations)

print("Lowest location number:", lowest_location)
