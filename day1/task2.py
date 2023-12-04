import re
from os import path
location = path.dirname(path.realpath(__file__))

f = open(file=f"{location}/input.txt")
sum_cali = 0
lines = f.read().splitlines()

num_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


# ex = '''two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen'''

# lines = ex.split('\n')

def convert_to_digit(text):
    if text in num_dict:
        return num_dict[text]
    else:
        return text


for line in lines:
    # Find all numbers (text and digits)
    matches = list(re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line))
    tensDigit = convert_to_digit(matches[0].group(1))
    onesDigit = convert_to_digit(matches[-1].group(1))
    number = int(tensDigit + onesDigit)

    sum_cali += number

print(sum_cali)
