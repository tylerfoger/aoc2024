input = 'day2-input.txt'

def generateReports():
    reports = []
    with open(input, 'r') as inputFile:
        for report in inputFile.readlines():
            reports.append(report)
    return reports


def safeReport(report):
    if (isAscOrDesc(report)): # and safeNeighbors(report)):
        return True
    else:
        return False

def isAscOrDesc(report):
    asc = report.split(' ')
    prevLevel = 0

    print('asc:')
    for level in asc:
        print(level)
        if int(level) < prevLevel:
            return False
        prevLevel = int(level)

    prevLevel = 0

    print('desc:')
    for level in reversed(asc):
        print(level)
        if int(level) < prevLevel:
            return False
        prevLevel = int(level)

    print('ascending or descending')
    return True

def safeNeighbors(report):
    pass
    #return True

reports = generateReports()


safeReportCount = 0

for report in reports:
    if safeReport(report):
       safeReportCount += 1
    else:
        print('not safe')

print(safeReportCount)
