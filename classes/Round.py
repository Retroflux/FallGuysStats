#Single instance of a game in Fall Guys

class Round:
	"""docstring for Course"""
	def __init__(self,name,startingParticipants,qualifyingParrticipants,roundNumber, episodeNumber,playerScore):
		super(Course, self).__init__()
		self._name = name
		self._startingParticipants = startingParticipants
		self._qualifyingParticipants = qualifyingParrticipants
		self._roundNumber = roundNumber
		self._episodeNumber = episodeNumber
		self._playerScore = playerScore

	


# Name
# Number of Participants
# Number of Winners
# Round number
# Episode number?
# Score
