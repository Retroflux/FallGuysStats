# Episode = full round of games from start to finish

# Number of rounds
# Episode Number
# Number of Team Games
# Number of Solo Games
# Final Placement Score

class Episode:
    """docstring for Episode"""
    totalNumberOfEpisodes = 0

    def __init__(self, numberOfRounds, episodeNumber, finalPlayerScore, listOfRounds, numberOfTeamGames=0, numberOfSoloGames=0):
        self._numberOfRounds = numberOfRounds
        self._episodeNumber = episodeNumber
        self._numberOfTeamGames = numberOfTeamGames
        self._numberOfSoloGames = numberOfSoloGames
        self._finalPlayerScore = finalPlayerScore
        self._listOfRounds = listOfRounds

    @property
    def numberOfRounds(self):
        return self._numberOfRounds

    @property
    def episodeNumber(self):
        return self._episodeNumber

    @property
    def numberOfTeamGames(self):
        return self._numberOfTeamGames

    @property
    def numberOfSoloGames(self):
        return self._numberOfSoloGames

    @property
    def finalPlayerScore(self):
        return self._finalPlayerScore

    @property
    def listOfRounds(self):
        return self._listOfRounds

    @numberOfRounds.setter
    def numberOfRounds(self,numberOfRounds):
        self._numberOfRounds = numberOfRounds

    @episodeNumber.setter
    def episodeNumber(self,episodeNumber):
        self._episodeNumber = episodeNumber

    @numberOfTeamGames.setter
    def numberOfTeamGames(self,numberOfTeamGames):
        self._numberOfTeamGames = numberOfTeamGames

    @numberOfSoloGames.setter
    def numberOfSoloGames(self,numberOfSoloGames):
        self._numberOfSoloGames = numberOfSoloGames

    @finalPlayerScore.setter
    def finalPlayerScore(self,finalPlayerScore):
        self._finalPlayerScore = finalPlayerScore

    @listOfRounds.setter
    def listOfRounds(self,listOfRounds):
        self._listOfRounds = listOfRounds
