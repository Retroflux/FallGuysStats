from generatePlayerObject import generatePlayerObjectFromFile
from generatePlayerObject import generatePlayerMetaStatistics


def main():
    playerNumber = 1
    playerObject = generatePlayerObjectFromFile("data/FallGuysStats.csv", playerNumber)
    playerObject = generatePlayerMetaStatistics(playerObject)
    outputPlayerStats(playerObject)
    return


def outputEpisodeListData(playerObject):
    for episode in playerObject.episodeList:
        print("EPISODE #" + str(episode.episodeNumber)+":")
        print("FINAL SCORE:" + str(episode.finalPlayerScore))
        for currentRound in episode.listOfRounds:
            print("\t" + currentRound.name + "; SCORE:" + str(currentRound.playerScore))


def outputPlayerStats(playerObject):
    for eventItem in playerObject.eventList:
        print("\tEVENT: " + eventItem.eventName)
        print("\t\tFrequency of Event Play: " + str(eventItem.frequencyOfEventPlay))
        # print("\t\tOn Average, this player places in the top %.3f%% of players in the games they "
        #       "play" % (eventItem.averageScoreAsAPercent * 100))
        print("\t\tNumber of Player Wins: " + str(eventItem.numberOfWins))
        print("\t\tNumber of Player Losses: " + str(eventItem.numberOfLosses))
        print("\t\tPlayer Win Percentage: " + str(
            eventItem.numberOfWins / (eventItem.numberOfWins + eventItem.numberOfLosses) * 100) + "%")
        print("\t\tOn Average, players with a percent score less than %.3f%% pass through this course." % (
                eventItem.theoreticalScoreAsAPercentage * 100))


if __name__ == '__main__':
    main()
