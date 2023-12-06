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
        time = int(lines[0].strip().split(':')[1].replace(" ", ""))  # Remove spaces and convert to int
        distance = int(lines[1].strip().split(':')[1].replace(" ", ""))  # Remove spaces and convert to int
        return time, distance

# Read data from file
file_name = 'input.txt'
time, distance = read_file(file_name)

total_ways = calculate_ways(time, distance)
print("Total number of ways to win the race:", total_ways)
