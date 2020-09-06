from classes.PlayerEvent import PlayerEvent

class Player:
    # TODO getter and setter for unique events
    totalUniqueEvents = 0

    def __init__(self, playerNumber):
        self._playerNumber = playerNumber
        self._episodeList = list()
        self._eventList = list()

    @property
    def playerNumber(self):
        return self._playerNumber

    @property
    def episodeList(self):
        return self._episodeList

    @property
    def eventList(self):
        return self._eventList

    @playerNumber.setter
    def playerNumber(self, playerNumber):
        self._playerNumber = playerNumber

    @episodeList.setter
    def episodeList(self, episodeList):
        self._episodeList = episodeList

    @eventList.setter
    def eventList(self,eventList):
        self._eventList = eventList
