from classes.Player import Player
from classes.Episode import Episode
from classes.Round import Round
from classes.PlayerEvent import PlayerEvent

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
        # TODO for each round, update the PlayerEvent list
        # TODO First, check to see if the event already exists in the list. If not, create new player event, add to list
        # TODO  else, update the PlayerEvent object that has the corresponding event name
            #TODO Add to the event frequency, number of wins/losses, average % needed to qualify
        for roundItem in roundObjectList:
            match = 0
            for i in range(playerObject.eventList):
                if roundItem.name == playerObject.eventList[i].eventName:
                    playerObject.eventList[i] = updatePlayerEvent(playerObject.eventList[i], roundItem)
                    match = 1

            if (match == 0):
                playerObject.eventList.append(PlayerEvent(roundItem.name))
        playerObject.episodeList.append(Episode(len(roundObjectList),episodeNumber,finalScore,roundObjectList))

    return playerObject


def updatePlayerEvent(eventObject, roundObject):
    # TODO: Fix sleepy brain code, need to calculate math and stuff here, replace variables
    tempCombinedPlayerScore = eventObject.frequencyOfEventPlay * eventObject.averageScoreAsAPercent
    eventObject.frequencyOfEventPlay += 1
    tempCombinedPlayerScore += roundObject.playerScore
    eventObject.averageScoreAsAPercent = tempCombinedPlayerScore / eventObject.frequencyOfEventPlay


    return eventObject


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
