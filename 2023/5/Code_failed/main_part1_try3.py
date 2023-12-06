def read_almanac_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def parse_map(map_str):
    conversion_map = {}
    count = 1
    for line in map_str.split('\n'):
        print(f"doing: {count}")
        count+=1
        if line.strip():
            dest_start, src_start, length = map(int, line.split())
            print(f"dest_start = {dest_start}, src_start = {src_start}, length = {length}")
            for i in range(length):
                conversion_map[src_start + i] = dest_start + i
    return conversion_map

def convert_number(number, conversion_map, memo):
    if number in memo:
        return memo[number]
    converted_number = conversion_map.get(number, number)
    memo[number] = converted_number
    return converted_number

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
    print("Parsing map")
    data_sections = almanac_data.split('\n\n')
    seeds = list(map(int, data_sections[0].split(':')[1].split()))

    maps = {}
    for section in data_sections[1:]:
        map_name, map_str = section.split(' map:\n')
        print(f"Parsing stuff: {map_name.strip()}")
        maps[map_name.strip()] = parse_map(map_str)
    
    return seeds, maps

# Example usage
file_path = 'almanac.txt'  # Replace with the actual file path
almanac_data = read_almanac_from_file(file_path)
seeds, maps = parse_almanac(almanac_data)
lowest_location = find_lowest_location(seeds, maps)
print(lowest_location)
