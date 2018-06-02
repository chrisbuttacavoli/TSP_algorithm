from tour import Tour


class Ant:
	def __init__(self, cities, startCity):
		self.currentCity = startCity
		self.id = startCity.id
		self.startCity = startCity
		self.tour = Tour(startCity)
		self.unvisitedCities = self._initUnvisitedCities(cities, startCity)
		self.APLHA = 0.2
		self.BETA = 0.6
		self.PHI = 0.75
	
#####################################################################################
# Helper functions and properties to make the rest easier to read
#####################################################################################
	@property
	def hasCompletedTour(self):
		return len(self.unvisitedCities) == 0 and \
				self.currentCity.id == self.startCity.id
	@property
	def hasNotCompletedTour(self):
		return not self.hasCompletedTour
	
	def isStartCity(self, city):
		return city.id == self.startCity.id
#####################################################################################
# Initialization functions
#####################################################################################
	# Returns a 1D array containing all cities except for the start city
	def _initUnvisitedCities(self, cities, startCity):
		unvisitedCities = list(cities)
		del unvisitedCities[startCity.id]
		return unvisitedCities


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
	def moveToNextCity(self, graph):
		# A safe-guard clause
		if self.hasCompletedTour:
			return
		
		prevCity = self.currentCity
		nextCity = self._getNextCity(graph)

		# Update the ant's tour
		distanceToNextCity = graph.distances[prevCity.id][nextCity.id]
		self.tour.addCityToTour(nextCity, distanceToNextCity)

		# Remove the next city from the unvisited list unless the list is empty
		self._removeCityFromUnvisitedCities(nextCity)

		# for lulz
		print("Ant " + str(self.id), "moved from", prevCity.id, "to", nextCity.id)

		# Place ant in the next city
		self.currentCity = nextCity

		# Update local pheromones on the edge we just travelled
		self._updateLocalPheromones(prevCity, self.currentCity)


	#####################################################################################
	# Compute the probability of each edge for city selection using the probabilistic
	# equation.
	# 
	# Input: Current city, graph
	# Output: 1D array of probability values
	#####################################################################################	
	def _computeProbability(self, currentCity, graph):
		denominator = 0

		for i in range(0, len(self.unvisitedCities)):
			unvisitedCity = self.unvisitedCities[i]
			pheromone = graph.pheromones[currentCity.id][unvisitedCity.id]
			distInvered = 1/graph.distances[currentCity.id][unvisitedCity.id]
			denominator += (pheromone**self.APLHA) * (distInvered**self.BETA)

		p = []
		for i in range(0, len(self.unvisitedCities)):
			unvisitedCity = self.unvisitedCities[i]
			pheromone = graph.pheromones[currentCity.id][unvisitedCity.id]
			distInvered = 1/graph.distances[currentCity.id][unvisitedCity.id]
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
				return self.unvisitedCities[i].id


	#####################################################################################
	# Returns the next city to be chosen from the graph
	#
	# Input: graph
	# Output: a city (unvisited)
	#####################################################################################
	def _getNextCity(self, graph):
		# If we have visited everything, go back to the start city
		if len(self.unvisitedCities) == 0:
			return self.startCity

		else:
			# Select the next city based on probabilities
			probabilities = self._computeProbability(self.currentCity, graph)
			nextCity = graph.cities[self._selectNextCityId(probabilities)]
			return nextCity


	def _removeCityFromUnvisitedCities(self, cityToRemove):
		if not self.isStartCity(cityToRemove):
			for i, city in enumerate(self.unvisitedCities):
				
				if city.id == cityToRemove.id:
					del self.unvisitedCities[i]
					break


	#####################################################################################
	# Places pheromones according to the formula in the report along the traversed edge
	#
	# Input: city1 and city2 (the cities that make up the edge)
	# Output: none
	#####################################################################################
	def _updateLocalPheromones(self, city1, city2):
		pass