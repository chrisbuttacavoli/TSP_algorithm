class City:
	def __init__(self, name, x, y):
		self.name = name
		self.x = x
		self.y = y


# Tracks path and length, probably a property of Ant
#class Tour:
	


class Ant:
	def __init__(self, numCities, startCity):
		self.visitedCities = []
		self.tourLength = 0
		self.path = []
	
	def visitedCity(param1, param2):
		pass