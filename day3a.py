import re

input_file = 'day3-input.txt'

def handle_input(input):
    output = ''
    with open(input, 'r') as inputFile:
        for line in inputFile.readlines():
            output += line
    return output

def filter_input(input):
    pattern = re.compile(r"mul\([0-9]+,[0-9]+\)")
    match = pattern.findall(input)
    return match

filtered_input = filter_input(handle_input(input_file))

total = 0
for item in filtered_input:
    getIntsPattern = re.compile(r"[0-9]+.*[0-9]+")
    getInts = getIntsPattern.findall(item)
    leftInt, rightInt = ' '.join(getInts).split(',')
    result = int(leftInt) * int(rightInt)
    total += result

print(total)
