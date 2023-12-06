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

def convert_number(number, ranges, memo):
    if number in memo:
        return memo[number]
    
    for src_start, src_end, dest_start in ranges:
        if src_start <= number < src_end:
            converted_number = number - src_start + dest_start
            memo[number] = converted_number
            return converted_number

    memo[number] = number
    return number

def process_seed(seed, maps, memos):
    for map_name in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
        seed = convert_number(seed, maps[map_name], memos[map_name])
    return seed

def find_lowest_location(seeds, maps):
    memos = {map_name: {} for map_name in maps}
    location_numbers = [process_seed(seed, maps, memos) for seed in seeds]
    return min(location_numbers)

# Function to parse the entire almanac data
def parse_almanac(almanac_data):
    data_sections = almanac_data.split('\n\n')
    seeds = list(map(int, data_sections[0].split(':')[1].split()))

    maps = {}
    for section in data_sections[1:]:
        map_name, map_str = section.split(' map:\n')
        maps[map_name.strip()] = parse_map(map_str)
    
    return seeds, maps

# Example usage
file_path = 'almanac.txt'  # Replace with the actual file path
almanac_data = read_almanac_from_file(file_path)
seeds, maps = parse_almanac(almanac_data)
lowest_location = find_lowest_location(seeds, maps)
print(lowest_location)
