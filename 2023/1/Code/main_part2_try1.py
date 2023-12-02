
## 1566

def calculate_calibration_value_from_file(file_path):
    total_sum = 0
    digit_mapping = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }

    def find_digit(s):
        for word, digit in digit_mapping.items():
            if word in s:
                return digit
        return None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            first_digit = find_digit(line)
            last_digit = find_digit(line[::-1])

            if first_digit is not None and last_digit is not None:
                total_sum += int(first_digit + last_digit)

    return total_sum

# Example usage
file_path = 'input.txt'  # Replace 'input.txt' with the path to your input file
result = calculate_calibration_value_from_file(file_path)
print("Total calibration value:", result)

'''
That's the right answer! You are one gold star closer to restoring snow operations.
...
Great! I'm glad to hear that the solution worked. If you have more puzzles or tasks to 
solve, feel free to share them. Let's continue working together to restore snow operations! 🌟🌨️
'''

'''Prompt
Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, 
two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:

two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

In this example, the calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.

Write a python script to perform this task. It should take an input usually from a file (in this 
case just those 7 lines. The input can be made of many lines of arbitrary length. Every line must be processed 
according to the above instructions and the final result must be displayed.
'''