class PlayerEvent:

    def __init__(self, eventName):
        self._eventName = eventName
        self._frequencyOfEventPlay = 1
        self._averageScoreAsAPercent = 0
        self._theoreticalScoreAsAPercentage = 0
        self._averagePercentScoreNeededToQualify = 0
        self._numberOfWins = 0
        self._numberOfLosses = 0

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
    def averagePercentScoreNeededToQualify(self):
        return self._averagePercentScoreNeededToQualify

    @property
    def numberOfWins(self):
        return self._numberOfWins

    @property
    def numberOfLosses(self):
        return self._numberOfLosses

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

    @averagePercentScoreNeededToQualify.setter
    def averagePercentScoreNeededToQualify(self, averagePercentScoreNeededToQualify):
        self._averagePercentScoreNeededToQualify = averagePercentScoreNeededToQualify

    @numberOfWins.setter
    def numberOfWins(self,numberOfWins):
        self._numberOfWins = numberOfWins

    @numberOfLosses.setter
    def numberOfLosses(self, numberOfLosses):
        self._numberOfLosses = numberOfLosses
