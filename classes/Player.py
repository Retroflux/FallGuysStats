#Player object that holds list of episodes and statistics

# noinspection PyPep8Naming
class Player:

    def __init__(self, playerNumber):
        self._playerNumber = playerNumber
        self._episodeList = list()

    @property
    def playerNumber(self):
        return self._playerNumber

    @property
    def episodeList(self):
        return self._episodeList

    @playerNumber.setter
    def playerNumber(self, playerNumber):
        self._playerNumber = playerNumber

    @episodeList.setter
    def episodeList(self, episodeList):
        self._episodeList = episodeList

