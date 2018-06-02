from parameters import Q, RHO, MIN_DIST, MIN_PHER


class Graph:
	def __init__(self, cities):
		self.distances, self.pheromones = self._initEdges(cities)
		self.cities = cities

		
	#####################################################################################
	# Performs a one time calculation between each city and stores it in an array
	#
	# Input: list of cities
	# Output: 2D, triangle array of distances between each city.
	#####################################################################################
	def _initEdges(self, cities):
		import math

		distances = []
		pheromones = []
		for i, fromCity in enumerate(cities):
			distanceRow = []
			pheromoneRow = []
			print("Creating city", i, "of", len(cities))
			for j in range(0, i):
				toCity = cities[j]
				temp = (fromCity.x - toCity.x)**2 + (fromCity.y - toCity.y)**2
				distance = int(math.sqrt(temp))
				if distance == 0:
					distance = MIN_DIST
				distanceRow.append(distance)
				pheromoneRow.append(MIN_PHER)
			
			distances.append(distanceRow)
			pheromones.append(pheromoneRow)
		return distances, pheromones


	#####################################################################################
	# We evaporate pheromones on all edges after each completed tour of all ants.
	# Reduces pheromones along each edge by some calculate with greek letters
	#
	# Input: nothing
	# Output: void
	#####################################################################################
	def _performEvaporation(self):
		for i in range(0, len(self.pheromones)):
			for j in range(0, i):
				self.pheromones[i][j] *= (1 - RHO)


	#####################################################################################
	# Updates the pheromones along each edge of the graph by looping all ants and using
	# the formula in the report
	#
	# Input: list of ants, list of cities
	# Output: void
	#####################################################################################
	def updatePheromones(self, ants, cities):
		# Evaporation should be performed first
		self._performEvaporation()

		# Go over each ant, look at their tour, add add pheromones to those edges
		for k, ant in enumerate(ants):
			# Loop over the ant's tour path and find the edge to update
			for pathIndex in range(len(ant.tour.path) - 1):
				# This update does not need to take into account the previous pheromones.
				# The evaporation function will deal with that
				fromCityId, toCityId = ant.tour.path[pathIndex], ant.tour.path[pathIndex + 1]

				if fromCityId > toCityId:
					self.pheromones[fromCityId][toCityId] += (Q / self.distances[fromCityId][toCityId])
				else:
					self.pheromones[toCityId][fromCityId] += (Q / self.distances[toCityId][fromCityId])