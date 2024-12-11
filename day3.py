import re

input_file = 'day3-input.txt'

def handleInput():
    output = ''
    with open(input_file, 'r') as inputFile:
        for line in inputFile.readlines():
            output += line

    return output

def filterFunctions(input_text):
    pattern = re.compile(r"[A-Za-z]+\([^)]*\)")
    matches = pattern.findall(input_text)
    return matches

def filterMultiply(input_text):
    pattern = re.compile(r"''mul\([^)]*\)'")
    combined_text = ' '.join(input_text)
    matches = pattern.findall(combined_text)
    return matches

text = handleInput()

allFunctions = filterFunctions(text)
multiplies = filterMultiply(allFunctions)

print(allFunctions)
print(multiplies)
