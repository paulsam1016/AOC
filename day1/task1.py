import re

x = open(file="input.txt")
sum_cali = 0
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
    first = re.search("\d", line)  # Find first digit
    reversedLine = line[::-1]  # Reverse String
    last = re.search("\d", reversedLine)  # Find last digit
    number = int(first[0] + last[0])

    sum_cali += number

print(sum_cali)
