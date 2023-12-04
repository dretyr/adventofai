# Scratchcard data from the example
scratchcards_example = [
    "41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    " 1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

def calculate_points(scratchcards):
    total_points = 0

    for card in scratchcards:
        winning_numbers, my_numbers = card.split("|")
        winning_numbers = set(map(int, winning_numbers.split()))
        my_numbers = set(map(int, my_numbers.split()))

        matches = winning_numbers.intersection(my_numbers)
        if matches:
            card_points = 1 << (len(matches) - 1)  # Calculate points using bitwise left shift for doubling
        else:
            card_points = 0

        total_points += card_points

    return total_points

# Calculate the total points for the example scratchcards
total_points_example = calculate_points(scratchcards_example)
print(total_points_example)

