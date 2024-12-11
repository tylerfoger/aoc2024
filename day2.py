input = 'day2-input.txt'

def generateReports():
    reports = []
    with open(input, 'r') as inputFile:
        for line in inputFile.readlines():
            report = [int(level) for level in line.strip().split()]
            reports.append(report)
    return reports

def safeReport(report):
    if isAscOrDesc(report) and safeNeighbors(report):
        return True
    return False

def fixReport(report):
    for i, level in enumerate(report):
        alteredReport = report.copy()
        alteredReport.pop(i)
        if safeReport(alteredReport):
            return True


def isAscOrDesc(report):
    ascending = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    descending = all(report[i] > report[i + 1] for i in range(len(report) - 1))

    return ascending or descending

def safeNeighbors(report):
    for i, level in enumerate(report):
        if i == 0:
            if not safeNeighbor(level, report[i + 1]):
                return False
            continue

        if i == len(report) - 1:
            if not safeNeighbor(level, report[i - 1]):
                return False
            continue

        leftNeighbor = report[i - 1]
        rightNeighbor = report[i + 1]

        if not safeNeighbor(level, leftNeighbor):
            return False

        if not safeNeighbor(level, rightNeighbor):
            return False

    return True

def safeNeighbor(level, neighbor):
    if not (1 <= abs(level - neighbor) <= 3):
        return False
    return True


reports = generateReports()
safeReportCount = 0

for report in reports:
    if safeReport(report):
        safeReportCount += 1
    elif fixReport(report):
        safeReportCount += 1


print(safeReportCount)
fixReport(reports)
