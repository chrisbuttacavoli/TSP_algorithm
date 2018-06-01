# This runs on Python 3
from ant import Ant
from city import City
from graph import Graph
from tour import Tour
from fileOperations import ReadCityData, OutputData
import sys
import math
from drawGraph import plotTour


def Main(inputFile):
	# Setup up our variables
	writeFile = "mytour" # + ".tour"
	numIterations = 1
	cities, cityIds = ReadCityData(inputFile)
	graph = Graph(cities, cityIds) # Each edge of the graph has its own pheromones
	bestTour = Tour(cities[0])
	bestTour.tourLength = float('inf')

	# This is our algorithm
	for n in range(0, numIterations):
		# New ants are placed at each city every iteration
		ants = [Ant(cityIds, startCity) for startCity in cities]
		for ant in ants:
			while ant.hasNotCompletedTour:
				ant.moveToNextCity(graph)
			bestTour = ReturnBestTour(ant.tour, bestTour)
		graph.updatePheromones(ants, cities)
	OutputData(writeFile, bestTour)


def ReturnBestTour(tour1, tour2):
	if tour1.tourLength > tour2.tourLength:
		return tour2
	return tour1


## i tried a matplot demo on flip, but
## it seems output figure cannot be displayed
## on filp due to the lack of GUI 
## we may replace this by a simple print
## -- Chris: We will remove this when we
## -- submit our code. This will just be for
## -- us to visually confirm our results
# plotTour(cities, bestTour)

# Allows us to put the Main() function at the top of the file
if __name__ == '__main__':
	Main(sys.argv[1])