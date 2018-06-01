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
		
		import random
		RHO = random.uniform(0, 1) #evaporation constant

		for i in range(0, len(self.pheromones)):
			for j in range(0, len(self.pheromones)):
				self.pheromones[i][j] = self.pheromones[i][j] * RHO

	#####################################################################################
	# Loops through each ant checking the cities they visited, then it will update
	# the concentration of the pheromones on each edge.
	#
	# Input: list of ants, list of cities
	# Output: void
	#####################################################################################
	def updatePheromones(ants, cities):
		self._performEvaporation()
		
		Q = 1.5 #constant that is arbitrarily assigned as a place holder
		
		for k in range(0, len(ants)):
			for i in range(0, len(self.pheromones)):
				for j in range(0, len(self.pheromones)):
					if(ants[k].currentCity == cities[i] and ants[k].nextCity == cities[j] ):
						Lk = _calculateDistances(cities[i], cities[j]) #length of the tour
						self.pheromones[i][j] += Q/Lk
						self.pheromones[j][i] = self.pheromones[i][j]
					else:
						pass
