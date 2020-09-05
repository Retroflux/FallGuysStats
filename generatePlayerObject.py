from classes.Player import Player
from classes.Episode import Episode
from classes.Round import Round

def generatePlayerObjectFromFile(filePath,playerNumber):
    print("hello world")
    headerRow = True

    CSV_Data = readListFromCSV(filePath)
    print (len(CSV_Data))
    playerObject = Player(playerNumber)

    for line in CSV_Data:
        if headerRow:
            headerRow = False
            continue
        print(line)
        (timestamp, episodeNumber, roundData, roundOut, finalScore) = isolateCellsWithRoundDataAggregated(line)
        roundObjectList = generateRoundObjects(roundData,episodeNumber)
        playerObject.episodeList.append(Episode(len(roundObjectList),episodeNumber,finalScore,roundObjectList))

    return playerObject


def readListFromCSV(filePath):
    tempList = list()
    with open(filePath, "r") as fileIn:
        for line in fileIn:
            tempList.append(line.strip())
    return tempList


def isolateCellsWithRoundDataAggregated(line):

     return(str(line.split(",")[0]), #timestamp
           str(line.split(",")[1]), #Episode number
           line.split(",")[2:19], #Round data; will be parsed separately later
           str(line.split(",")[20]), #Round out
           str(line.split(",")[21]), #Final score
    )


def generateRoundObjects(roundData,episodeNumber):
    roundObjects = list()
    roundCounter = 1
    remainingRoundData = roundData
    while True:
        currRound = remainingRoundData[:4]
        if (currRound[1] == "" or roundCounter >=6):
            break
        tempRoundObj = Round(currRound[1], currRound[0], currRound[3], roundCounter, episodeNumber, currRound[2])
        roundObjects.append(tempRoundObj)

        roundCounter += 1
        remainingRoundData = remainingRoundData[3:]
    return roundObjects


def verifyRoundNames(roundObj):
    # TODO verification of round names``
    pass
