from generatePlayerObject import generatePlayerObjectFromFile


def main():
    playerNumber = 1

    playerObject = generatePlayerObjectFromFile("data/FallGuysStats.csv", playerNumber)

    for episode in playerObject.episodeList:
        print("EPISODE #" + str(episode.episodeNumber)+":")
        print("FINAL SCORE:" + str(episode.finalPlayerScore))
        for currentRound in episode.listOfRounds:
            print("\t" + currentRound.name + "; SCORE:" + str(currentRound.playerScore))
    return


if __name__ == '__main__':
    main()