# This runs on Python 2
from classes import City

#!!!ADDED BY HYOUNG" - For graph functionality
from collections import defaultdict
import sys

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
cities, distances = ReadCityData()
ants = InitializeAnts(cities, distances)
for n in range(1, numIterations):
	bestTour = PerformTour(ants, cities, distances)

OutputData(bestTour)
###########################


# ReadCityData
# ### Reads data from a text file, outputs a list of
# ### cities and a their distances to each other city.
# ### Not sure what the most efficient way to store
# ### the distance matrix so I'll leave that up to you.
# ### Calculate the distances based on Project
# ### Instructions.

def ReadCityData():
    #Get input file from the command line
    #Ref: https://anenadic.github.io/2014-11-10-manchester/novice/python/06-cmdline-non-interactive.html
    script = sys.argv[0]
    fileName = sys.argv[1]
	
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
# End of ReadCityData
#####################################################################################



#####################################################################################
# CalcDistance(cityA, cityB)
#
# Takes two elements from the cities list then outputs distance between them
#
# ARGUMENTS: two elements from cities list from ReadCityData()
# RETURNS:   distance between two cities
#####################################################################################
import math
def CalcDistance(cityA, cityB):
    x = cityA[1] - cityB[1]
    y = cityA[2] - cityB[2]

    temp = (x*x)+(y*y)
    distance = int(math.sqrt(temp))

    return(distance)

#####################################################################################
#
# End of CalcDistance
#
#####################################################################################



# Initialize Ants
# ### Should place an ant starting at each city.


# PerformTour
# ### This will execute N times until we are happy with
# ### the optimal solution or run out of time/iterations.
# ### This binds the algorithm together after everything
# ### has been initialized.


# MoveAnt
# ### Uses a probability function based on next closest
# ### city and the amount of pheromones on each path
# ### adjacent to the current city to choose the next
# ### city. For now, this can just be randomly determined
# ### until we work out details for the other functions.


# UpdatePheromones
# ### After an ant completes a tour, two things happen.
# ### First, the previous pheromones that were laid
# ### begin to evaporate. Second, new pheromones are
# ### laid by each ant for the paths that they took.


# OutputData
# ### Outputs a file:
# ### First line is the total length of the tour.
# ### Second line and onward is the ordered name of
# ### cities, so each city gets its own lines
# ### Name of output file: {inputFileName.txt}.tour
