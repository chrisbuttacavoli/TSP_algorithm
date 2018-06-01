# This runs on Python 3
from ant import Ant
from city import City
from graph import Graph
from tour import Tour
from fileOperations import ReadCityData, OutputData
import sys
import math
from drawGraph import plotTour


def ReturnBestTour(tour1, tour2):
	if tour1.tourLength > tour2.tourLength:
		return tour2
	return tour1


###########################
# Main procedure below...
###########################
###########################

# Setup up our variables
readFile = sys.argv[1]
writeFile = "mytour" # + ".tour"
numIterations = 1
cities, cityIds = ReadCityData(readFile)
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


## i tried a matplot demo on flip, but
## it seems output figure cannot be displayed
## on filp due to the lack of GUI 
## we may replace this by a simple print
## -- Chris: We will remove this when we
## -- submit our code. This will just be for
## -- us to visually confirm our results
# plotTour(cities, bestTour)