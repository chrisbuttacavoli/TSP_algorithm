class Graph:
	def __init__(self, cities):
		self.distances, self.pheromones = self._initEdges(cities) # Insert Hyoung's original function here
		self.cities = cities
		self.Q = 1.5

		
	#####################################################################################
	# Performs a one time calculation between each city and stores it in a 2D array
	#
	# Input: list of cities
	# Output: 2D array of distances between each city
	#####################################################################################
	def _initEdges(self, cities):
		import math

		distances = []
		pheromones = []
		for i, city1 in enumerate(cities):
			distanceRow = []
			pheromoneRow = []
			for j, city2 in enumerate(cities):
				temp = (city1.x * city1.x) + (city2.y * city2.y)
				distance = int(math.sqrt(temp))
				distanceRow.append(distance)
				pheromoneRow.append(1)
			
			distances.append(distanceRow)
			pheromones.append(pheromoneRow)
		return distances, pheromones


	#####################################################################################
	# Updates the pheromones along each edge of the graph by looping all ants and using
	# the formula in the report
	#
	# Input: list of ants, list of cities
	# Output: void
	#####################################################################################
	def updatePheromones(self, ants, cities):	
		
		import math
		Q = 1 # constant moved to property of the graph class
		for k in range(0, len(ants)):
			for i in range(0, len(self.pheromones)):
				for j in range(0, len(self.pheromones)):
					if(ants[k].tour.path[-2] == cities[i].id and ants[k].tour.path[-1] == cities[j].id ):
						x = cities[i].x - cities[j].x 				
						y = cities[i].y - cities[j].y
						temp = (x**2) + (y**2)
						
						Lk = int(math.sqrt(temp)) #length of the tour
						
						self.pheromones[i][j] += Q/Lk
						self.pheromones[j][i] = self.pheromones[i][j]
				else:
					pass
				
		# Q = 1.5 # constant moved to property of the graph class
		
		# for k in range(0, len(ants)):
		# 	for i in range(0, len(self.pheromones)):
		# 		for j in range(0, len(self.pheromones)):
		# 			if(ants[k].currentCity == cities[i] and ants[k].nextCity == cities[j] ):
		# 				Lk = _calculateDistances(cities[i], cities[j]) #length of the tour
		# 				self.pheromones[i][j] += Q/Lk
		# 				self.pheromones[j][i] = self.pheromones[i][j]
		# 			else:
		# 				pass
		
