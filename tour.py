from parameters import MIN_DIST


# Tracks path and length of an ant's tour.
class Tour:
	def __init__(self, startCity):
		self.tourLength = 0
		self.path = [startCity.id]
		self.cumulativeTourLength = []
	

	#####################################################################################
	# Adds a cityId to the path and increases the tourLength by the distance.
	# Should throw an error if trying to travel to a city that is already in the tour
	#
	# Inputs:
	#	- cityId: the id of the desired city to travel to
	#	- distance: the distance to the city to travel to
	# Outputs: void
	#####################################################################################
	def addCityToTour(self, city, distance):
		self.path.append(city.id)
		if distance != MIN_DIST:
			self.tourLength = self.tourLength + distance