class City:
	def __init__(self, id, x, y):
		self.id = id
		self.x = x
		self.y = y


# Tracks path and length, of a tour.
class Tour:
	def __init__(self):
		self.tourLength = 0
		self.path = []
	
	def addCityToTour(cityId, distance):
		self.path.append(cityId)
		self.tourLength = self.tourLength + distance


# Knows about which cities have already been visited
class Ant:
	def __init__(self, numCities, startCity):
		self.visitedCities = []
		self.tour = Tour()
	
	def visitCity(cityId):
		# There should be some logic in here to prevent an
		# ant from visited a city it has already visited
		pass


class Pheromones:
	def __init__(self, cities):
		# This is a 2-D array tracking the concentration of pheromones along each edge
		self.concentrations = [[0 for i in range(len(cities))] for j in range(len(cities))]

	# We evaporate some of the pheromones after each tour is complete
	def evaporate():
		pass
	
	# Check the path of each edge and add pheromones to it
	def addPheromonesToEdge(fromCityId, toCityId):
		# I just realized that we only need half the 2-D array
		# since 2 edges actually are the same edge...maybe you
		# can figure out a smarter way to avoid this? It is a
		# constant time operation though, so it may not matter.
		# Right now I am incrementing by 1, but that is just a
		# placeholder that will be changed later.
		self.concentrations[fromCityId, toCityId] = self.concentrations[fromCityId, toCityId] + 1
		self.concentrations[toCityId, fromCityId] = self.concentrations[toCityId, fromCityId] + 1
