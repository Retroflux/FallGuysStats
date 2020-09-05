#Single instance of a game in Fall Guys

class Round:
	"""docstring for Course"""
	def __init__(self, name, startingParticipants, qualifyingParticipants, roundNumber, episodeNumber, playerScore):
		self._name = name
		self._startingParticipants = startingParticipants
		self._qualifyingParticipants = qualifyingParticipants
		self._roundNumber = roundNumber
		self._episodeNumber = episodeNumber
		self._playerScore = playerScore

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
	
	@name.setter
	def name(self,name):
		self._name = name

	@startingParticipants.setter
	def startingParticipants(self,startingParticipants):
		self._startingParticipants=startingParticipants

	@qualifyingParticipants.setter
	def qualifyingParticipants(self,qualifyingParticipants):
		self._qualifyingParticipants = qualifyingParticipants

	@roundNumber.setter
	def roundNumber(self,roundNumber):
		self._roundNumber = roundNumber

	@episodeNumber.setter
	def episodeNumber(self,episodeNumber):
		self._episodeNubmer = episodeNumber

	@playerScore.setter
	def playerScore(self,playerScore):
		self._playerScore = playerScore


# Name
# Number of Participants
# Number of Winners
# Round number
# Episode number?
# Score
