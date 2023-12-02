'''
That's the right answer! You are one gold star closer to restoring snow operations.
...

Fantastic! I'm glad we could solve the puzzle correctly. If you have more challenges or puzzles, 
feel free to share them. Let's continue working together towards restoring snow operations. 🌟🌨️
'''

## Result: 53592

def calculate_calibration_value_from_file(file_path):
    total_sum = 0
    digit_words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digit_mapping = {word: str(index + 1) for index, word in enumerate(digit_words)}

    def find_first_digit(s):
        for i in range(len(s)):
            if s[i].isdigit():
                return s[i]
            for word in digit_words:
                if s[i:].startswith(word):
                    return digit_mapping[word]
        return None

    def find_last_digit(s):
        for i in range(len(s) - 1, -1, -1):
            if s[i].isdigit():
                return s[i]
            for word in digit_words:
                # Reverse the string and word for last digit check
                if s[:i + 1][::-1].startswith(word[::-1]):
                    return digit_mapping[word]
        return None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            first_digit = find_first_digit(line)
            last_digit = find_last_digit(line)

            if first_digit is not None and last_digit is not None:
                total_sum += int(first_digit + last_digit)

    return total_sum

# Example usage
file_path = 'input.txt'  # Replace 'input.txt' with the path to your input file
result = calculate_calibration_value_from_file(file_path)
print("Total calibration value:", result)



''' Prompt
User
That's not the right answer; your answer is too low. 
This looks very similar to the previous one. In reviewing the sub-function extract_digits, 
it appears you are finding the word, but not necessarily the "first" or the "last" word 
that represent digits. How could this function be updated to ensure that it is always the 
first word or first digit and the last word or last digit being used.
'''