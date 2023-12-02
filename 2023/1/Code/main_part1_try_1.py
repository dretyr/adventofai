
## Result 55621

def calculate_calibration_value(lines):
    total_sum = 0

    for line in lines:
        first_digit = None
        last_digit = None

        # Find the first digit
        for char in line:
            if char.isdigit():
                first_digit = char
                break

        # Find the last digit
        for char in reversed(line):
            if char.isdigit():
                last_digit = char
                break

        # Combine the digits and add to total sum
        if first_digit and last_digit:
            total_sum += int(first_digit + last_digit)

    return total_sum

# Example usage
input_lines = [
    "1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"
]

# result = calculate_calibration_value(input_lines)
# print("Total calibration value:", result)

def calculate_calibration_value_from_file(file_path):
    total_sum = 0

    with open(file_path, 'r') as file:
        for line in file:
            first_digit = None
            last_digit = None

            # Find the first digit
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break

            # Find the last digit
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break

            # Combine the digits and add to total sum
            if first_digit and last_digit:
                total_sum += int(first_digit + last_digit)

    return total_sum

# Example usage
file_path = 'input.txt'  # Replace 'input.txt' with the path to your input file
result = calculate_calibration_value_from_file(file_path)
print("Total calibration value:", result)


'''Prompt edit for file input
Instead of replacing the lines with an input, change the script to take the input lines from a file.
'''

''' Prompt
Something is wrong with global snow production, and you've been selected to take a look. The Elves have even given you a map; on it, they've used stars to mark the top fifty locations that are likely to be having problems.

You've been doing this long enough to know that to restore snow operations, you need to check all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You try to ask why they can't just use a weather machine ("not powerful enough") and where they're even sending you ("the sky") and why your map looks mostly blank ("you sure ask a lot of questions") and hang on did you just say the sky ("of course, where do you think snow comes from") when you realize that the Elves are already loading you into a trebuchet ("please hold still, we need to strap you in").

As they're making the final adjustments, they discover that their calibration document (your puzzle input) has been amended by a very young Elf who was apparently just excited to show off her art skills. Consequently, the Elves are having trouble reading the values on the document.

The newly-improved calibration document consists of lines of text; each line originally contained a specific calibration value that the Elves now need to recover. On each line, the calibration value can be found by combining the first digit and the last digit (in that order) to form a single two-digit number.

For example:

1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.
Write a python script to perform this task. It should take an input usually from a file (in this case just those 4 lines. The can be made of many lines of arbitrary length. Every line must be processed according to the above instructions and the final result must be displayed.
'''