import re
from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
lines = f.read().splitlines()

sum_cali = 0

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
