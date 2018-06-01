from tour import Tour


class Ant:
	def __init__(self, cityIds, startCity):
		self.currentCity = startCity
		self.id = startCity.id
		self.startCity = startCity
		self.tour = Tour(startCity)
		self.unvisitedCityIds = self._initUnvisitedCityIds(cityIds, startCity)
		self.APLHA = 0.2
		self.BETA = 0.6
	
#####################################################################################
# Helper functions and properties to make the rest easier to read
#####################################################################################
	@property
	def hasCompletedTour(self):
		return len(self.unvisitedCityIds) == 0 and \
				self.currentCity.id == self.startCity.id
	@property
	def hasNotCompletedTour(self):
		return not self.hasCompletedTour
	
	def isStartCity(self, city):
		return city.id == self.startCity.id

	#####################################################################################
	# This function will need to be decomposed into smaller functions to achieve
	# the following:
	# - selects the city to travel to. must be a cityId in the unvisitedCityIds
	#		collection.
	# - updates its Tour to include the new tour length and the path
	#
	# Input: 2D graph containing distances between cities and pheromone values
	# Output: void
	#####################################################################################
	def moveToNextCity(self, graph):
		# A safe-guard clause
		if self.hasCompletedTour:
			return
		
		nextCity = self._getNextCity(graph)

		# Update the ant's tour
		distanceToNextCity = graph.distances[self.currentCity.id][nextCity.id]
		self.tour.addCityToTour(nextCity, distanceToNextCity)

		# Remove the next city from the unvisited list
		if not self.isStartCity(nextCity):
			self.unvisitedCityIds.remove(nextCity.id)

		print("Ant " + str(self.id), "moved from", self.currentCity.id, "to", nextCity.id)

		# Place ant in the next city
		self.currentCity = nextCity


	#####################################################################################
	# Initializes the unvisited cities 
	# 
	# Input: list of city ids, the starting city
	# Output: 1D array with size n-1 that contains the cities' ids minus the start city id
	# (n = the number of cities in the example.txt)
	#####################################################################################	
	def _initUnvisitedCityIds(self, cityIds, startCity):
		unvisitedCityIds = list(cityIds)
		unvisitedCityIds.remove(startCity.id)
		return unvisitedCityIds


	#####################################################################################
	# Compute the probability of each edge for city selection using the probabilistic
	# equation.
	# 
	# Input: Current city, graph
	# Output: 1D array of probability values
	#####################################################################################	
	def _computeProbability(self, currentCity, graph):
		denominator = 0

		for i in range(0, len(self.unvisitedCityIds)):
			unvisitedCity = self.unvisitedCityIds[i]
			pheromone = graph.pheromones[currentCity.id][unvisitedCity]
			distInvered = 1/graph.distances[currentCity.id][unvisitedCity]
			denominator += (pheromone**self.APLHA) * (distInvered**self.BETA)

		p = []
		for i in range(0, len(self.unvisitedCityIds)):
			unvisitedCity = self.unvisitedCityIds[i]
			pheromone = graph.pheromones[currentCity.id][unvisitedCity]
			distInvered = 1/graph.distances[currentCity.id][unvisitedCity]
			p.append((pheromone**self.APLHA) * (distInvered**self.BETA) / denominator)

		return p


	#####################################################################################
	# Select the next city by comparing a random number (between 0 to 1) with an 
	# accumulator. The accumulator will accumulate the calculated probability list,
	# starting from index 0. We will choose the city in which the
	# accumulator >= the random number.
	#
	# Input: probability list ; 
	# Output: the index of the next city that the ant will travel
	#####################################################################################	
	def _selectNextCityId(self, probabilities):
		import random

		# random float between 0 - 1 (including 0 and 1)
		x = random.uniform(0, 1)

		accumulator = 0 # use to compare with the random float
		for i in range(0, len(probabilities)):
			accumulator += probabilities[i]
			if accumulator >= x:
				return self.unvisitedCityIds[i]


	#####################################################################################
	# Returns the next city to be chosen from the graph
	#
	# Input: graph
	# Output: a city (unvisited)
	#####################################################################################
	def _getNextCity(self, graph):
		# If we have visited everything, go back to the start city
		if len(self.unvisitedCityIds) == 0:
			return self.startCity

		else:
			# Select the next city based on probabilities
			probabilities = self._computeProbability(self.currentCity, graph)
			nextCity = graph.cities[self._selectNextCityId(probabilities)]
			return nextCity