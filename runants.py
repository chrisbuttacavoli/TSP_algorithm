# This runs on Python 3
from classes import City
import sys
import math


# Main is somewhere over here
city = City(8, 9)
print city.x, city.y

##########
# OUTLINE
##########
# These high level steps are a first pass at what our
# program would be composed of. These functions are
# guidelines and can be adjusted as needed. We should
# strongly consider moving them to other files to keep
# main looking "clean".
#####################


###########################
# Main goes below...
###########################
###########################

# Goes something like so...
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


#####################################################################################
# ReadCityData(fileName)
#
# Populates a list of cities from a text file per Instructions.pdf
#
# Inputs: the name of the file to read from
# Outputs: a list of cities
#####################################################################################
def ReadCityData(fileName):	
    #Read data from a target file
    #Ref: https://stackoverflow.com/questions/29581804/python-reading-input-from-a-file
    cities =[] 

    with open(fileName, "r") as file: 
        for line in file:

            line = line.split()
            if line:
                    line = [int(i) for i in line]  #converts elements to integers
                    cities.append(line)
    return(cities)


#####################################################################################
# CalcDistance(cityA, cityB)
#
# Takes two elements from the cities list then outputs distance between them
#
# Inputs: two elements from cities list from ReadCityData()
# Outputs: distance between two cities
#####################################################################################
def CalcDistance(cityA, cityB):
    x = cityA[1] - cityB[1]
    y = cityA[2] - cityB[2]

    temp = (x*x)+(y*y)
    distance = int(math.sqrt(temp))

    return(distance)



#####################################################################################
# OutputData(fileName, tour)
# Outputs a file:
# - First line is the total length of the tour.
# - Second line and onward is the ordered name of cities, so each city gets
# 		its own lines
# - Name of output file: {inputFileName.txt}.tour
#
# Inputs:
# - fileName: Name of the file to get the data from
# - tour: The tour data, as a Tour class
#####################################################################################
def OutputData(fileName, tour):
	pass