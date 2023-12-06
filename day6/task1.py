from os import path

location = path.dirname(path.realpath(__file__))
IS_SAMPLE = True

if IS_SAMPLE:
    f = open(file=f"{location}/sample.txt")
else:
    f = open(file=f"{location}/input.txt")
inputs = f.read().splitlines()

times = list(map(int, inputs[0].split()[1:]))
distances = list(map(int, inputs[1].split()[1:]))
margin_of_error = 1

for record_time, record_distance in zip(times, distances):
    # print(record_time, record_distance)
    check_time = 1
    possible_times = []
    while check_time < record_time:
        if check_time * (record_time-check_time) > record_distance:
            possible_times.append(check_time)
        check_time += 1
    # print(possible_times)
    margin_of_error *= len(possible_times)

print(f'margin of error: {margin_of_error}')
