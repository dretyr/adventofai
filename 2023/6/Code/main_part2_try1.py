def calculate_ways(time, distance):
    ways_to_win = 0
    for hold_time in range(time):
        travel_time = time - hold_time
        speed = hold_time
        total_distance = speed * travel_time
        if total_distance > distance:
            ways_to_win += 1
    return ways_to_win

# Single race data from modified input
time = 71530
distance = 940200

total_ways = calculate_ways(time, distance)
print("Total number of ways to win the race:", total_ways)
