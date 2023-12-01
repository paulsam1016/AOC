import re

x = open(file="input.txt")
sum = 0
lines = x.readlines()

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

    first = re.search("\d", string)  # Find first digit
    line = line[::-1]  # Reverse String
    last = re.search("\d", line)  # Find last digit
    number = int(first[0] + last[0])

    sum += number

print(sum)
