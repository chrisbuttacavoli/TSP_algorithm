# This runs on Python 3
from ant import Ant
from city import City
from graph import Graph
from tour import Tour
from fileOperations import ReadCityData, OutputData
import sys
import math


###########################
# Main procedure below...
###########################
###########################

numIterations = 20
cities = ReadCityData(sys.argv[1])
graph = Graph(cities) # Each edge of the graph has its own pheromones
ants = [Ant(len(cities), city) for city in cities] # Start an ant at each city

for n in range(1, numIterations):
	for ant in ants:
		while ant.hasNotCompletedTour:
			ant.move(graph)
		bestTour = SelectBestTour(ant.tour, bestTour)
	
	graph.updatePheromones(ants)

OutputData(bestTour)
###########################