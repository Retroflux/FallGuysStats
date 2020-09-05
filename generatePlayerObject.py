from classes.Player import Player
from classes.Episode import Episode
import csv
import os
import sys


def main():
    print("hello world")

    CSV_Data = readListFromCSV("data/FallGuysStats.csv")

    playerObject = Player(1)
    print(playerObject.playerNumber)

    for line in CSV_Data:
        print(line)
        # TODO isolate the required cell information
        # TODO create a process to isolate a round object data pack, and determine a way to access the final score
        # playerObject.episodeList.append(Episode)

    # TODO import csv file from hardcoded location
    # TODO generate Player object
    # TODO iterate through each line of the file, extracting objects along the way
    # TODO output results to stdout

    return


def readListFromCSV(filePath):
    tempList = list()
    with open(filePath, "r") as fileIn:
        for line in fileIn:
            tempList.append(line.strip())
    return tempList


if __name__ == '__main__':
    main()
