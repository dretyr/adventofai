def read_scratchcards_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()

def count_matching_numbers(winning_numbers, your_numbers):
    return len(winning_numbers.intersection(your_numbers))

def process_scratchcards(scratchcards):
    total_cards = len(scratchcards)
    won_cards = [0] * total_cards  # Track won cards for each original card

    for i, card in enumerate(scratchcards):
        parts = card.split(" | ")
        winning_numbers = set(map(int, parts[0].split()))
        your_numbers = set(map(int, parts[1].split()))

        matches = count_matching_numbers(winning_numbers, your_numbers)
        for j in range(i + 1, min(i + 1 + matches, total_cards)):
            won_cards[j] += 1

    # Process the won cards recursively
    while any(won_cards):
        new_won_cards = [0] * total_cards
        for i, count in enumerate(won_cards):
            if count > 0:
                parts = scratchcards[i].split(" | ")
                winning_numbers = set(map(int, parts[0].split()))
                your_numbers = set(map(int, parts[1].split()))

                matches = count_matching_numbers(winning_numbers, your_numbers)
                for j in range(i + 1, min(i + 1 + matches, total_cards)):
                    new_won_cards[j] += count

        total_cards += sum(won_cards)
        won_cards = new_won_cards

    return total_cards

# Example usage
file_path = 'scratchcard_data.txt'
scratchcards = read_scratchcards_from_file(file_path)
total_scratchcards = process_scratchcards(scratchcards)
print(total_scratchcards)
