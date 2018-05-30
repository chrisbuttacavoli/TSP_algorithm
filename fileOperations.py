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
# OutputData(fileName, tour)
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
	pass

