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
	numIterations = 50
	cities = ReadCityData(inputFile)
	graph = Graph(cities) # Each edge of the graph has its own pheromones
	bestTour = Tour(cities[0])
	bestTour.tourLength = float('inf')

	# This is our algorithm
	for n in range(0, numIterations):
		print("Iteration", n + 1, "of", numIterations)
		# New ants are placed at each city every iteration
		ants = [Ant(cities, startCity) for startCity in cities]
		for ant in ants:
			while ant.hasNotCompletedTour:
				ant.moveToNextCity(graph)
			bestTour = ReturnBestTour(ant.tour, bestTour)
		graph.updatePheromones(ants, cities)
	OutputData(writeFile, bestTour)
	plotTour(cities, bestTour) #may comment it out when submitting to Canvas


def ReturnBestTour(tour1, tour2):
	if tour1.tourLength > tour2.tourLength:
		return tour2
	print("Best tour is now", tour1.tourLength)
	return tour1


# Allows us to put the Main() function at the top of the file
if __name__ == '__main__':
	Main(sys.argv[1])