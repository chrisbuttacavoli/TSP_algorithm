#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <stdlib.h> 
#include <time.h> 
#include <limits>

#include "parameters.h"

using namespace std;

class Ant {
public:
	int numCities;
	int startCityId;
	int currentCityId;
	int tourLength;
	vector<int> tour;
	vector<bool> unvisitedCities; //to record whether or not a city is visited
	int numUnvisitedCities;

	Ant(int startCityId, int numCities) {
		this->numCities = numCities;
		this->startCityId = startCityId;
		this->currentCityId = startCityId;
		this->tourLength = 0;
		this->tour.push_back(startCityId);
		this->numUnvisitedCities = numCities - 1;

		// Fill an array value boolean values representing if we have visited the city
		// If the position == the startCity ID, say we have visited it already with false
		for (int i = 0; i < numCities; i++) {
			if (i == startCityId)
				this->unvisitedCities.push_back(false);
			else
				this->unvisitedCities.push_back(true);
		}

	}
	
	void moveToNextCity(int** distances, double** pheromones) {
		int prevCityId = currentCityId;
		int nextCityId = _getNextCity(distances, pheromones);
		
		// Update the ant's tour
		int distanceToAdd = distances[prevCityId][nextCityId];
		if (distanceToAdd == 0)
			distanceToAdd = MIN_DIST;
		tourLength += distanceToAdd;
		tour.push_back(nextCityId);
	
		// Set the next city in unvisitedCities to false
		unvisitedCities[nextCityId] = false;

		// Decrement the number of unvisited cities
		numUnvisitedCities--;

		// Place ant in the next city
		currentCityId = nextCityId;
	}
	
	vector<double> _computeProbability(int currentCityId, int** distances, double** pheromones) {
		double denominator = 0;
		vector<double> probabilities;

		// Figure out the denominator to be used for each city
		for (int cityId = 0; cityId < numCities; cityId++) {
			double nij;
			double Tij;
			double temp;

			if (unvisitedCities[cityId] == true){
				nij = 1 / (double) distances[currentCityId][cityId];
				Tij = pheromones[currentCityId][cityId];
				temp = pow(Tij, ALPHA)*pow(nij, BETA);
				probabilities.push_back(temp);
				denominator += temp;
			}
			else {
				probabilities.push_back(0);
			}
		}

		// compute the probability for each city
		for (int cityId = 0; cityId < numCities; cityId++) {
			if (unvisitedCities[cityId] == true)
				probabilities[cityId] = probabilities[cityId] / denominator;
			else
				probabilities[cityId] = 0;
		}
		return probabilities;
	}

	
	int _selectNextCityId(vector<double> p){
		// Pick random number between 0 and 1
		double x = ((double)rand() / (double)RAND_MAX);
		double accumulator = 0;
		
		for (int i = 0; i < numCities; i++) {
			accumulator += p[i];
			if (accumulator >= x)
				return i;
		}
	}


	int _getNextCity(int** distances, double** pheromones) {
		//If we have visited everything, go back to the start city
		if (numUnvisitedCities == 0)
			return startCityId;
		else {
			//Select the next city based on probabilities
			int nextCityId = _selectNextCityId(_computeProbability(currentCityId,distances,pheromones));
			return nextCityId;
		}
	}
};