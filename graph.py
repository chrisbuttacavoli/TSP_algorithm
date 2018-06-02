from parameters import Q, RHO, MIN_DIST, MIN_PHER


class Graph:
	def __init__(self, cities):
		self.distances, self.pheromones = self._initEdges(cities) # Insert Hyoung's original function here
		self.cities = cities

		
	#####################################################################################
	# Performs a one time calculation between each city and stores it in a 2D array
	#
	# Input: list of cities
	# Output: 2D array of distances between each city
	#####################################################################################
	def _initEdges(self, cities):
		import math

		distances = [[0] * len(cities) for _ in cities]
		pheromones = [[MIN_PHER] * len(cities) for _ in cities]
		for i, fromCity in enumerate(cities):
			for j in range(0, i):
				toCity = cities[j]
				temp = (fromCity.x - toCity.x)**2 + (fromCity.y - toCity.y)**2
				distance = int(math.sqrt(temp))
				if distance == 0:
					distance = MIN_DIST
				distances[fromCity.id][toCity.id] = distance
				distances[toCity.id][fromCity.id] = distance
		return distances, pheromones


	#####################################################################################
	# We evaporate pheromones on all edges after each completed tour of all ants.
	# Reduces phermones along each edge by some calculate with greek letters
	#
	# Input: nothing
	# Output: void
	#####################################################################################
	def _performEvaporation(self):
		for i in range(0, len(self.pheromones)):
			for j in range(0, i):
				self.pheromones[i][j] = (1 - RHO) * self.pheromones[i][j]
				self.pheromones[j][i] = self.pheromones[i][j]


	#####################################################################################
	# Updates the pheromones along each edge of the graph by looping all ants and using
	# the formula in the report
	#
	# Input: list of ants, list of cities
	# Output: void
	#####################################################################################
	def updatePheromones(self, ants, cities):			
		# import math

		# Evaporation should be performed first
		self._performEvaporation()

		# Go over each ant, look at their tour, add add pheromones to those edges
		for k, ant in enumerate(ants):
			# Loop over the ant's tour path and find the edge to update
			for pathIndex in range(len(ant.tour.path) - 1):
				# This update does not need to take into account the previous pheromones.
				# The evaporation function will deal with that
				fromCityId, toCityId = ant.tour.path[pathIndex], ant.tour.path[pathIndex + 1]
				deltaTijk = Q / self.distances[fromCityId][toCityId]
				self.pheromones[fromCityId][toCityId] += deltaTijk
				self.pheromones[toCityId][fromCityId] = self.pheromones[fromCityId][toCityId]