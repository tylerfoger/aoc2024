input = 'day1-input.txt'


def createLists():
    leftList = []
    rightList = []

    with open(input, 'r') as inputFile:
        for line in inputFile.readlines():
            lineText = line.split(' ')
            leftList.append(int(lineText[0]))
            rightList.append(int(lineText[3].replace('\n', '')))

    return leftList, rightList


def getTotalDistance(lists):
    print(lists)
    totalDistance = 0
    leftList = sorted(lists[0], reverse=True)
    rightList = sorted(lists[1], reverse=True)

    for i in range(len(leftList)):
        difference = leftList[i] - rightList[i]

        if difference < 0:
            difference *= -1
        
        totalDistance += difference

    return totalDistance


totalDistance = getTotalDistance(createLists())

print(totalDistance)
