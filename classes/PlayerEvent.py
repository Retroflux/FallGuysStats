class PlayerEvent:

    def __init__(self, eventName):
        self._eventName = eventName
        self._frequencyOfEventPlay = 0
        self._averageScoreAsAPercent = 0
        self._theoreticalScoreAsAPercentage = 0
        self._numberScoresUsedForTheoreticalScorePercentage = 0
        self._numberOfWins = 0
        self._numberOfLosses = 0
        self._minStartingPlayers = 99
        self._maxStartingPlayers = 1

    @property
    def eventName(self):
        return self._eventName

    @property
    def frequencyOfEventPlay(self):
        return self._frequencyOfEventPlay

    @property
    def averageScoreAsAPercent(self):
        return self._averageScoreAsAPercent

    @property
    def theoreticalScoreAsAPercentage(self):
        return self._theoreticalScoreAsAPercentage

    @property
    def numberScoresUsedForTheoreticalScorePercentage(self):
        return self._numberScoresUsedForTheoreticalScorePercentage

    @property
    def numberOfWins(self):
        return self._numberOfWins

    @property
    def numberOfLosses(self):
        return self._numberOfLosses

    @property
    def minStartingPlayers(self):
        return self._minStartingPlayers

    @property
    def maxStartingPlayers(self):
        return self._maxStartingPlayers

    @eventName.setter
    def eventName(self, eventName):
        self._eventName = eventName

    @frequencyOfEventPlay.setter
    def frequencyOfEventPlay(self, frequencyOfEventPlay):
        self._frequencyOfEventPlay = frequencyOfEventPlay

    @averageScoreAsAPercent.setter
    def averageScoreAsAPercent(self, averageScoreAsAPercent):
        self._averageScoreAsAPercent = averageScoreAsAPercent

    @theoreticalScoreAsAPercentage.setter
    def theoreticalScoreAsAPercentage(self, theoreticalScoreAsAPercentage):
        self._theoreticalScoreAsAPercentage = theoreticalScoreAsAPercentage

    @numberScoresUsedForTheoreticalScorePercentage.setter
    def numberScoresUsedForTheoreticalScorePercentage(self, numberScoresUsedForTheoreticalScorePercentage):
        self._numberScoresUsedForTheoreticalScorePercentage = numberScoresUsedForTheoreticalScorePercentage

    @numberOfWins.setter
    def numberOfWins(self, numberOfWins):
        self._numberOfWins = numberOfWins

    @numberOfLosses.setter
    def numberOfLosses(self, numberOfLosses):
        self._numberOfLosses = numberOfLosses

    @minStartingPlayers.setter
    def minStartingPlayers(self, minStartingPlayers):
        self._minStartingPlayers = minStartingPlayers

    @maxStartingPlayers.setter
    def maxStartingPlayers(self, maxStartingPlayers):
        self._maxStartingPlayers = maxStartingPlayers
