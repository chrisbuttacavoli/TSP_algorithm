class City:
	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y


# Tracks path and length of an ant's tour.
class Tour:
	def __init__(self):
		self.tourLength = 0
		self.path = []
	

	#####################################################################################
	# Adds a cityId to the path and increases the tourLength by the distance.
	# Should throw an error if trying to travel to a city that is already in the tour
	#
	# Inputs:
	#	- cityId: the id of the desired city to travel to
	#	- distance: the distance to the city to travel to
	# Outputs: void
	#####################################################################################
	def addCityToTour(cityId, distance):
		self.path.append(cityId)
		self.tourLength = self.tourLength + distance


class Ant:
	def __init__(self, numCities, startCity):
		self.hasNotCompletedTour = True
		self.unvisitedCities = []
		self.tour = Tour()
	

	#####################################################################################
	# This function will need to be decomposed into smaller functions to achieve
	# the following:
	# - selects the city to travel to. must be a cityId in the unvisitedCities
	#		collection.
	# - updates its Tour to include the new tour length and the path
	#
	# Input: 2D graph containing distances between cities and pheromone values
	# Output: void
	#####################################################################################
	def move(graph):
		# For now we can just randomly pick a city until we work out pheromone
		# probabilities which seems to be a big lift.
		pass


class Graph:
	def __init__(self, cities):
		self.pheromones = _initPheromones(cities)
		self.distances = _calculateDistances(cities) # Insert Hyoung's original function here


	#####################################################################################
	# Performs a one time calculation between each city and stores it in a 2D array
	#
	# Input: list of cities
	# Output: 2D array of distances between each city
	#####################################################################################
	def _calculateDistances(cities):
		pass

	
	#####################################################################################
	# Initializes a 2D array with values of 0. The return array represents an edge
	# graph containing all pheromone values between each city.
	#
	# Input: list of cities
	# Output: 2D array of 0's sized by the list of cities. Should start with a
	#	value of 0 for each edge since no ant has traversed anything yet.
	#####################################################################################
	def _initPheromones(cities):
		pass


	#####################################################################################
	# We evaporate pheromones on all edges after each completed tour of all ants.
	# Reduces phermones along each edge by some calculate with greek letters
	#
	# Input: nothing
	# Output: void
	#####################################################################################
	def _performEvaporation():
		pass
	

	#####################################################################################
	# Loops through each ant checking the cities they visited, then it will update
	# the concentration of the pheromones on each edge.
	#
	# Input: list of ants
	# Output: void
	#####################################################################################
	def updatePheromones(ants):
		self._performEvaporation()

		# Do other stuff
		pass