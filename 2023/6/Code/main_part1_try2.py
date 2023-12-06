def calculate_ways(time, distance):
    ways_to_win = 0
    for hold_time in range(time):
        travel_time = time - hold_time
        speed = hold_time
        total_distance = speed * travel_time
        if total_distance > distance:
            ways_to_win += 1
    return ways_to_win

def read_file(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        times = [int(time) for time in lines[0].strip().split()[1:]]  # Skip the 'Time:' part
        distances = [int(distance) for distance in lines[1].strip().split()[1:]]  # Skip the 'Distance:' part
        return list(zip(times, distances))

# Read data from file
file_name = 'input.txt'
race_data = read_file(file_name)

total_ways = 1
for time, distance in race_data:
    ways = calculate_ways(time, distance)
    total_ways *= ways

print("Total number of ways to win all races:", total_ways)
