# Episode = full round of games from start to finish

# Number of rounds
# Episode Number
# Number of Team Games
# Number of Solo Games
# Final Placement Score

class Episode():
    """docstring for Episode"""

    def __init__(self, numberOfRounds, episodeNumber, numberOfTeamGames, numberOfSoloGames, finalPlayerScore):
        self._numberOfRounds = numberOfRounds
        self._episodeNumber = episodeNumber
        self._numberOfTeamGames = numberOfTeamGames
        self._numberOfSoloGames = numberOfSoloGames
        self._finalPlayerScore = finalPlayerScore
