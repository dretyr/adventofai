
## Result 47458

def calculate_calibration_value_from_file(file_path):
    total_sum = 0
    digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digit_mapping = {word: str(index + 1) for index, word in enumerate(digit_words)}

    def extract_digits(s):
        for word in digit_words:
            if word in s:
                return s.replace(word, digit_mapping[word], 1)
        return s

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            line = extract_digits(line)
            line = extract_digits(line[::-1][::-1])

            digits = [char for char in line if char.isdigit()]
            if len(digits) >= 2:
                first_digit, last_digit = digits[0], digits[-1]
                total_sum += int(first_digit + last_digit)

    return total_sum

# Example usage
file_path = 'input.txt'  # Replace 'input.txt' with the path to your input file
result = calculate_calibration_value_from_file(file_path)
print("Total calibration value:", result)

'''
That's not the right answer; your answer is too low.
'''