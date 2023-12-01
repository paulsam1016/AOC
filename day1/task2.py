import re

x = open(file="input.txt")
sum = 0
lines = x.readlines()

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

for line in lines:
    string = line

    # Find all numbers (text and digits)
    matches = re.finditer(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', string)
    found_texts = []
    for match in matches:
        number = match.group(1)
        # Convert all text numbers to digits
        if number in num_dict:
            found_texts.append(num_dict[number])
        else:
            found_texts.append(number)
    number = int(found_texts[0] + found_texts[-1])

    sum += number

print(sum)
