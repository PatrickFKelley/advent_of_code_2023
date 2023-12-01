import re

NUM_CONVERTER = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def calibrate(line, pattern):
    calibration_nums = pattern.findall(line)
    calibration_nums = [NUM_CONVERTER.get(x) if not x.isdigit() else x
                        for x in calibration_nums]
    return int(calibration_nums[0] + calibration_nums[-1])


# -------------------------------- Data Input --------------------------------

with open('day_01/input.txt') as input:
    calibration_lines = [line for line in input.readlines()]
    
# --------------------------------- Part One ---------------------------------

p1_pattern = re.compile('\d')

p1_answer = sum(calibrate(line, p1_pattern) for line in calibration_lines)

print(f'The sum of all calibration values is {p1_answer}')

# --------------------------------- Part Two ---------------------------------

p2_pattern = re.compile('(?=(\d|one|two|three|four|five|six|seven|eight|nine))')

p2_answer = sum(calibrate(line, p2_pattern) for line in calibration_lines)

print(f'The sum of all revised calibration values is {p2_answer}')