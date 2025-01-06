from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = False

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
inputs = f.read().splitlines()

times = [int(''.join(inputs[0].split()[1:]))]
distances = [int(''.join(inputs[1].split()[1:]))]
margin_of_error = 1

# print(times)
# print(distances)

for record_time, record_distance in zip(times, distances):
    # Possible times are always continuous
    # [11, 12, 13, 14, 15, 16, 17, 18, 19]
    # Its possible to find the time limits
    lower_check_time = 1
    while lower_check_time < record_time:
        if lower_check_time * (record_time - lower_check_time) > record_distance:
            break
        lower_check_time += 1
    upper_check_time = record_time
    while upper_check_time > 0:
        if upper_check_time * (record_time - upper_check_time) > record_distance:
            break
        upper_check_time -= 1
    # print(lower_check_time, upper_check_time)
    margin_of_error *= (upper_check_time - lower_check_time + 1)

print(f'margin of error: {margin_of_error}')
