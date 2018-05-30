class City:
	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y


# Tracks path and length of an ant's tour.
class Tour:
	def __init__(self, startCity):
		self.tourLength = 0
		self.path = [startCity]
	

	#####################################################################################
	# Adds a cityId to the path and increases the tourLength by the distance.
	# Should throw an error if trying to travel to a city that is already in the tour
	#
	# Inputs:
	#	- cityId: the id of the desired city to travel to
	#	- distance: the distance to the city to travel to
	# Outputs: void
	#####################################################################################
	def addCityToTour(self, cityId, distance):
		self.path.append(cityId)
		self.tourLength = self.tourLength + distance


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
		
		#iteratively travel to the city until all city are visited
		while len(self.unvisitedCities)>0 :
			# compute the probablitites
			currentCity = self.startCity
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



class Graph:
	def __init__(self, cities):
		self.pheromones = self._initPheromones(cities)
		self.distances = self._calculateDistances(cities) # Insert Hyoung's original function here

		
	#####################################################################################
	# Performs a one time calculation between each city and stores it in a 2D array
	#
	# Input: list of cities
	# Output: 2D array of distances between each city
	#####################################################################################
	def _calculateDistances(self, cities):
		import math
		array2d = []
		for i in range(0, len(cities)):
			newElement = []
			for j in range(0, len(cities)):
				x = cities[i][1] - cities[j][1]
				y = cities[i][2] - cities[j][2]
				temp = (x*x) + (y*y)
				distance = int(math.sqrt(temp))
				newElement.append(distance)
			array2d.append(newElement)

		return(array2d)

	
	#####################################################################################
	# Initializes a 2D array with values of 0. The return array represents an edge
	# graph containing all pheromone values between each city.
	#
	# Input: list of cities
	# Output: 2D array of a certain value sized by the list of cities. This value cannot 
	# be 0 since that will result in 0 denominator for the probabilistic equation.
	# (let's use 1 as placeholder and do some fine tune later)
	#####################################################################################
	def _initPheromones(self, cities):
		import math
		pheromone2dArray = []
		for i in range(0, len(cities)):
			newElement = []
			for j in range(0, len(cities)):
				newElement.append(1)
			pheromone2dArray.append(newElement)

		return(pheromone2dArray)


	#####################################################################################
	# We evaporate pheromones on all edges after each completed tour of all ants.
	# Reduces phermones along each edge by some calculate with greek letters
	#
	# Input: nothing
	# Output: void
	#####################################################################################
	def _performEvaporation():
		for i in range(0, len(self.pheromone)):
			for j in range(0, len(self.pheromone)):
				if self.phermone[i][j] > 0:
					self.phermone[i][j] = self.phermone[i][j] - 1
				
	

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
