class Ant:
	def __init__(self, numCities, startCity):
		self.hasNotCompletedTour = True
		self.unvisitedCities = self._initUnvisitedCities(numCities, startCity)
		self.tour = Tour(startCity)
		self.startCity = startCity
		self.APLHA = 0.2
		self.BETA = 0.6
	

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
	def move(self, graph):
		currentCity = self.startCity
		
		#iteratively travel to the city until all city are visited
		while len(self.unvisitedCities)>0 :
			# compute the probablitites
			p = self._computeProbability(currentCity, graph)

			# select the next city 
			nextCity = self._selectCity(p)

			# update tour
			distanceToAdd = graph.distances[currentCity][nextCity]
			self.tour.addCityToTour(nextCity, distanceToAdd)

			# remove the next city from the unvisited list
			self.unvisitedCities.remove(nextCity)

			# set new current city
			currentCity = nextCity

		# the tour ends at the start city
		finalHome = self.startCity
		distanceToAdd = graph.distances[currentCity][finalHome]
		self.tour.addCityToTour(finalHome, distanceToAdd)


	#####################################################################################
	# Initializes the unvisited cities 
	# 
	#
	# Input: number of cities, index of start city
	# Output: 1D array with size n-1 that contains the cities' index except the start city
	# (n = the number of cities in the example.txt)
	#####################################################################################	
	def _initUnvisitedCities(self, numCities, startCity):
		tempArray = []
		for i in range(0, numCities):
			tempArray.append(i)

		tempArray.remove(startCity)

		return tempArray


	#####################################################################################
	# compute the probability of each edge for city selection using the probabilistic
	# equation.
	# 
	# Input: current city index ; graph
	# Output: 1D array of probability value
	#####################################################################################	
	def _computeProbability(self, currentCity, graph):
		denominator = 0

		for i in range(0, len(self.unvisitedCities)):
			unvisitedCity = self.unvisitedCities[i]
			pheromone = graph.pheromones[currentCity][unvisitedCity]
			distInvered = 1/graph.distances[currentCity][unvisitedCity]
			denominator += (pheromone**self.APLHA) * (distInvered**self.BETA)

		p = []
		for i in range(0, len(self.unvisitedCities)):
			unvisitedCity = self.unvisitedCities[i]
			pheromone = graph.pheromones[currentCity][unvisitedCity]
			distInvered = 1/graph.distances[currentCity][unvisitedCity]
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
	def _selectCity(self, probabilities):
		import random

		# random float between 0 - 1 (including 0 and 1)
		x = random.uniform(0, 1)

		accumulator = 0 # use to compare with the random float
		for i in range(0, len(probabilities)):
			accumulator += probabilities[i]
			if accumulator >= x:
				return self.unvisitedCities[i]