#####################################################################################
# plotTour(cities, path, tourLength)
#
# Plot the tour path and cities using matplotlib 
# (to install matplotlib: https://matplotlib.org/users/installing.html)
# 
# We may not submit this file to Canvas. Just use it for visualization.
#
# Inputs: list of city, list of tour path, length of tour
# Outputs: plot
#####################################################################################
import matplotlib.pyplot as plt

def plotTour(cities, path, tourLength):
	#size of the graph
	plt.figure(figsize=(10,7))

	#plot cities
	plt.plot([row[1] for row in cities],[row[2] for row in cities],'rx', markersize=3)

	#label the cities
	for i, row in enumerate(cities):
	    plt.annotate(row[0], (row[1], row[2]), size=8)

	#plot the tour
	for i in range(0,len(path)-1):
	    x1 = cities[path[i]][1]
	    y1 = cities[path[i]][2]
	    x2 = cities[path[i+1]][1]
	    y2 = cities[path[i+1]][2]
	    plt.plot([x1, x2],[y1, y2],'c-',linewidth=0.5)

	#title
	textstr = "Best tour = " + str(tourLength)
	plt.title(textstr)

	plt.show()