from city import City


#####################################################################################
# Populates a list of cities from a text file per Instructions.pdf
#
# Inputs: the name of the file to read from
# Outputs: a list of cities and cityIds
#####################################################################################
def ReadCityData(fileName):
	cities = []
	with open(fileName, "r") as file:
		for line in file:
			line = line.split()
			if line:
				line = [int(i) for i in line]  #converts elements to integers
				cities.append(City(line[0], line[1], line[2]))
	return cities


#####################################################################################
# Outputs the best tour to a file.
#
# Inputs:
# - fileName: Name of the file to get the data from
# - tour: The tour data, as a Tour class
# Outputs: a file containing:
# - First line is the total length of the tour.
# - Second line and onward is the ordered name of cities, so each city gets
# 		its own lines
# - Name of output file: {inputFileName.txt}.tour
#####################################################################################
def OutputData(fileName, tour):
	with open(fileName, "w") as file:
		file.write(str(tour.tourLength))
		alreadyWroteFirstCityToFile = False
		firstCityId = tour.path[0]
		for cityId in tour.path:
			if alreadyWroteFirstCityToFile and cityId == firstCityId:
				pass
			else:
				file.write("\n" + str(cityId))
				alreadyWroteFirstCityToFile = True