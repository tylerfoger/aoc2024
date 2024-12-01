input = 'day1-input.txt'


def createLists():
    leftList = []
    rightList = []

    with open(input, 'r') as inputFile:
        for line in inputFile.readlines():
            lineText = line.split(' ')
            leftList.append(int(lineText[0]))
            rightList.append(int(lineText[3].replace('\n', '')))

    return sorted(leftList, reverse=True),  sorted(rightList, reverse=True)


def getSimilarityScore(lists):
    similarityScore = 0
    leftList = lists[0]
    rightList = lists[1]

    for i in range(len(leftList)):
        id = leftList[i]
        instancesOfId = 0

        for distance in range(len(rightList)):

            if id == rightList[distance]:
                instancesOfId += 1
        
        similarityScore += (id * instancesOfId)


    return similarityScore


similarityScore = getSimilarityScore(createLists())

print(similarityScore)

