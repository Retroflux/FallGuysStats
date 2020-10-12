class Round:
    """docstring for Course"""

    def __init__(self, name, startingParticipants, qualifyingParticipants, roundNumber, episodeNumber, playerScore):
        self._name = name
        self._startingParticipants = startingParticipants
        self._qualifyingParticipants = qualifyingParticipants
        self._roundNumber = roundNumber
        self._episodeNumber = episodeNumber
        self._playerScore = playerScore
        self._playerAdvanced = True

    @property
    def name(self):
        return self._name

    @property
    def startingParticipants(self):
        return self._startingParticipants

    @property
    def qualifyingParticipants(self):
        return self._qualifyingParticipants

    @property
    def roundNumber(self):
        return self._roundNumber

    @property
    def episodeNumber(self):
        return self._episodeNumber

    @property
    def playerScore(self):
        return self._playerScore

    @property
    def playerAdvanced(self):
        return self._playerAdvanced

    @name.setter
    def name(self, name):
        self._name = name

    @startingParticipants.setter
    def startingParticipants(self, startingParticipants):
        self._startingParticipants = startingParticipants

    @qualifyingParticipants.setter
    def qualifyingParticipants(self, qualifyingParticipants):
        self._qualifyingParticipants = qualifyingParticipants

    @roundNumber.setter
    def roundNumber(self, roundNumber):
        self._roundNumber = roundNumber

    @episodeNumber.setter
    def episodeNumber(self, episodeNumber):
        self.episodeNumber = episodeNumber

    @playerScore.setter
    def playerScore(self, playerScore):
        self._playerScore = playerScore

    @playerAdvanced.setter
    def playerAdvanced(self, playerAdvanced):
        self._playerAdvanced = playerAdvanced

# Name
# Number of Participants
# Number of Winners
# Round number
# Episode number?
# Score
