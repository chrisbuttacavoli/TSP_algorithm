#####################################################################################
# plotTour(cities, tour)
#
# Plot the tour path and cities using matplotlib 
# (to install matplotlib: https://matplotlib.org/users/installing.html)
# 
# We may not submit this file to Canvas. Just use it for visualization.
#
# Inputs: list of cities, a tour
# Outputs: plot
#####################################################################################
import matplotlib.pyplot as plt


def plotTour(cities, tour):
	#size of the graph
	plt.figure(figsize=(10,7))

	#plot cities
	plt.plot([city.x for city in cities],[city.y for city in cities],'rx', markersize=3)

	#label the cities
	# for i, row in enumerate(cities):
	#     plt.annotate(row[0], (row[1], row[2]), size=8)

	#plot the tour
	for i in range(0,len(tour.path)-1):
	    x1 = cities[tour.path[i]].x
	    y1 = cities[tour.path[i]].y
	    x2 = cities[tour.path[i+1]].x
	    y2 = cities[tour.path[i+1]].y
	    plt.plot([x1, x2],[y1, y2],'c-',linewidth=0.5)

	#title
	textstr = "Best tour = " + str(tour.tourLength)
	plt.title(textstr)

	plt.show()