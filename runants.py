# This runs on Python 3
from classes import City, Graph, Ant
from fileOperations import ReadCityData, OutputData
import sys
import math
from drawGraph import plotTour

###########################
# Main procedure below...
###########################
###########################

bestTourLength = float('inf')
numIterations = 20
cities = ReadCityData(sys.argv[1])
graph = Graph(cities) # Each edge of the graph has its own pheromones
ants = [Ant(len(cities), city) for city in cities] # Start an ant at each city

for n in range(1, numIterations):
	for ant in ants:
		ant.move(graph)
		#update best tour
		if(ant.tour.tourLength < bestTourLength):
            bestTourLength = ant.tour.tourLength
            bestPath = ant.tour.path
	
	graph.updatePheromones(ants)


## i tried a matplot demo on flip, but
## it seems output figure cannot be displayed
## on filp due to the lack of GUI 
## we may replace this by a simple print
plotTour(cities, bestPath, bestTourLength)

###########################