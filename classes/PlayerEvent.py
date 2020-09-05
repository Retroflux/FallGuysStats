#A single event type, not a specific round

class PlayerEvent:

    def __init__(self, eventName):
        self._eventName = eventName
        self._frequencyOfEventPlay = 1
        self._averageScoreAsAPercent = 0
        self._theoreticalScoreAsAPercentage = 0
        self._averagePercentScoreNeededToQualify = 0
        self._numberOfWins = 0
        self._numberOfLosses = 0


