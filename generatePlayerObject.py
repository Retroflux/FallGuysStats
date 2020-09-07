from classes.Player import Player
from classes.Episode import Episode
from classes.Round import Round
from classes.PlayerEvent import PlayerEvent


def generatePlayerObjectFromFile(filePath, playerNumber):
    headerRow = True
    CSV_Data = readListFromCSV(filePath)
    playerObject = Player(playerNumber)

    for line in CSV_Data:
        if headerRow:
            headerRow = False
            continue
        # print(line)
        (timestamp, episodeNumber, roundData, roundOut, finalScore) = isolateCellsWithRoundDataAggregated(line)
        roundObjectList = generateRoundObjects(roundData, episodeNumber)
        playerObject.episodeList.append(Episode(len(roundObjectList), episodeNumber, finalScore, roundObjectList))
    return playerObject


def generatePlayerMetaStatistics(playerObject):
    finalRoundNamesList = readListFromCSV("data/finalRoundNames.txt")
    for episode in playerObject.episodeList:
        finalRoundFlag = False
        for roundItem in episode.listOfRounds:
            match = 0
            if roundItem.name in finalRoundNamesList:
                finalRoundFlag = True
            for i in range(len(playerObject.eventList)):
                if roundItem.name == playerObject.eventList[i].eventName:  # already exists
                    playerObject.eventList[i] = updateFrequencyAndScoreStats(playerObject.eventList[i], roundItem)
                    playerObject.eventList[i] = updateWinsAndLosses(playerObject.eventList[i], roundItem)
                    playerObject.eventList[i] = updateTheoreticalEventPercentages(playerObject.eventList[i], roundItem,
                                                                                  finalRoundFlag)
                    match = 1
                    # break
            if match == 0:
                playerObject.eventList.append(PlayerEvent(roundItem.name))
                playerObject.eventList[-1] = updateFrequencyAndScoreStats(playerObject.eventList[-1], roundItem)
                playerObject.eventList[-1] = updateWinsAndLosses(playerObject.eventList[-1], roundItem)
                playerObject.eventList[-1] = updateTheoreticalEventPercentages(playerObject.eventList[-1], roundItem,
                                                                               finalRoundFlag)
    return playerObject


def updateFrequencyAndScoreStats(eventObject, roundObject):
    if roundObject.playerScore != "" and roundObject.startingParticipants != "":
        tempCombinedPlayerScore = eventObject.frequencyOfEventPlay * eventObject.averageScoreAsAPercent
        eventObject.frequencyOfEventPlay += 1
        tempCombinedPlayerScore += float(roundObject.playerScore) / float(roundObject.startingParticipants)
        eventObject.averageScoreAsAPercent = tempCombinedPlayerScore / float(eventObject.frequencyOfEventPlay)
        if eventObject.eventName == "Jinxed":
            print()
            print(roundObject.playerScore)
            print(roundObject.startingParticipants)
            print(float(roundObject.playerScore) / float(roundObject.startingParticipants))
            print(tempCombinedPlayerScore)
            print(eventObject.averageScoreAsAPercent)
    return eventObject


def updateWinsAndLosses(eventObject, roundObject):
    # win/losses
    if roundObject.qualifyingParticipants == "":
        if roundObject.playerScore != "":
            if int(roundObject.playerScore) == 1:
                eventObject.numberOfWins += 1
            else:
                eventObject.numberOfLosses += 1
        else:
            eventObject.numberOfLosses += 1
    elif roundObject.qualifyingParticipants != "":
        if roundObject.qualifyingParticipants >= roundObject.playerScore:
            eventObject.numberOfWins += 1
        else:
            eventObject.numberOfLosses += 1
    return eventObject


def updateTheoreticalEventPercentages(eventObject, roundObject, finalRoundFlag):
    # NOTE must omit first round in the average % score needed to qualify because the numbers are not accurate.
    tempTheoreticalPercentSummation = eventObject.theoreticalScoreAsAPercentage * (
        eventObject.numberScoresUsedForTheoreticalScorePercentage)
    if roundObject.qualifyingParticipants == "":
        if finalRoundFlag:
            tempTheoreticalPercentSummation += (1 / int(roundObject.startingParticipants))
            eventObject.numberScoresUsedForTheoreticalScorePercentage += 1
            eventObject.theoreticalScoreAsAPercentage = tempTheoreticalPercentSummation / eventObject.numberScoresUsedForTheoreticalScorePercentage
    else:
        tempTheoreticalPercentSummation += (
                int(roundObject.qualifyingParticipants) / int(roundObject.startingParticipants))
        eventObject.numberScoresUsedForTheoreticalScorePercentage += 1
        eventObject.theoreticalScoreAsAPercentage = tempTheoreticalPercentSummation / eventObject.numberScoresUsedForTheoreticalScorePercentage
    return eventObject


def readListFromCSV(filePath):
    tempList = list()
    with open(filePath, "r") as fileIn:
        for line in fileIn:
            tempList.append(line.strip())
    return tempList


def isolateCellsWithRoundDataAggregated(line):
    return (str(line.split(",")[0]),  # timestamp
            str(line.split(",")[1]),  # Episode number
            line.split(",")[2:19],  # Round data; will be parsed separately later
            str(line.split(",")[20]),  # Round out
            str(line.split(",")[21]),  # Final score
            )


def generateRoundObjects(roundData, episodeNumber):
    roundObjects = list()
    roundCounter = 1
    remainingRoundData = roundData
    while True:
        currRound = remainingRoundData[:4]
        if currRound[1] == "" or roundCounter >= 6:
            break
        tempRoundObj = Round(currRound[1], currRound[0], currRound[3], roundCounter, episodeNumber, currRound[2])
        roundObjects.append(tempRoundObj)

        roundCounter += 1
        remainingRoundData = remainingRoundData[3:]
    return roundObjects


def verifyRoundNames(roundObj, roundNames):
    return True if roundObj.name in roundNames else False
