def calculate_ways(time, distance):
    ways_to_win = 0
    for hold_time in range(time):
        travel_time = time - hold_time
        speed = hold_time
        total_distance = speed * travel_time
        if total_distance > distance:
            ways_to_win += 1
    return ways_to_win

# Example data
races = [
    {"time": 7, "distance": 9},
    {"time": 15, "distance": 40},
    {"time": 30, "distance": 200}
]

total_ways = 1
for race in races:
    ways = calculate_ways(race["time"], race["distance"])
    total_ways *= ways

print("Total number of ways to win all races:", total_ways)
