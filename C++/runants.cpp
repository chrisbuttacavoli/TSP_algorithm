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

#include "city.h"
#include "ant.h"
#include "parameters.h"

using namespace std;

class Tour {
	int tourLength = 0;
	vector<int> path;
};


// class Ant {
// public:
// 	int numCities;
// 	int startCityId;
// 	int currentCityId;
// 	int tourLength;
// 	vector<int> tour;
// 	vector<bool> unvisitedCities; //to record whether or not a city is visited
// 	int numUnvisitedCities;

// 	Ant(int startCityId, int numCities) {
// 		this->numCities = numCities;
// 		this->startCityId = startCityId;
// 		this->currentCityId = startCityId;
// 		this->tourLength = 0;
// 		this->tour.push_back(startCityId);
// 		this->numUnvisitedCities = numCities - 1;

// 		// Fill an array value boolean values representing if we have visited the city
// 		// If the position == the startCity ID, say we have visited it already with false
// 		for (int i = 0; i < numCities; i++) {
// 			if (i == startCityId)
// 				this->unvisitedCities.push_back(false);
// 			else
// 				this->unvisitedCities.push_back(true);
// 		}

// 	}
	
// 	void moveToNextCity(int** distances, double** pheromones) {
// 		int prevCityId = currentCityId;
// 		int nextCityId = _getNextCity(distances, pheromones);
		
// 		// Update the ant's tour
// 		int distanceToAdd = distances[prevCityId][nextCityId];
// 		if (distanceToAdd == 0)
// 			distanceToAdd = MIN_DIST;
// 		tourLength += distanceToAdd;
// 		tour.push_back(nextCityId);
	
// 		// Set the next city in unvisitedCities to false
// 		unvisitedCities[nextCityId] = false;

// 		// Decrement the number of unvisited cities
// 		numUnvisitedCities--;

// 		// Place ant in the next city
// 		currentCityId = nextCityId;
// 	}
	
// 	vector<double> _computeProbability(int currentCityId, int** distances, double** pheromones) {
// 		double denominator = 0;
// 		vector<double> probabilities;

// 		// Figure out the denominator to be used for each city
// 		for (int cityId = 0; cityId < numCities; cityId++) {
// 			double nij;
// 			double Tij;
// 			double temp;

// 			if (unvisitedCities[cityId] == true){
// 				nij = 1 / (double) distances[currentCityId][cityId];
// 				Tij = pheromones[currentCityId][cityId];
// 				temp = pow(Tij, ALPHA)*pow(nij, BETA);
// 				probabilities.push_back(temp);
// 				denominator += temp;
// 			}
// 			else {
// 				probabilities.push_back(0);
// 			}
// 		}

// 		// compute the probability for each city
// 		for (int cityId = 0; cityId < numCities; cityId++) {
// 			if (unvisitedCities[cityId] == true)
// 				probabilities[cityId] = probabilities[cityId] / denominator;
// 			else
// 				probabilities[cityId] = 0;
// 		}
// 		return probabilities;
// 	}

	
// 	int _selectNextCityId(vector<double> p){
// 		// Pick random number between 0 and 1
// 		double x = ((double)rand() / (double)RAND_MAX);
// 		double accumulator = 0;
		
// 		for (int i = 0; i < numCities; i++) {
// 			accumulator += p[i];
// 			if (accumulator >= x)
// 				return i;
// 		}
// 	}


// 	int _getNextCity(int** distances, double** pheromones) {
// 		//If we have visited everything, go back to the start city
// 		if (numUnvisitedCities == 0)
// 			return startCityId;
// 		else {
// 		//Aelect the next city based on probabilities
// 			int nextCityId = _selectNextCityId(_computeProbability(currentCityId,distances,pheromones));
// 			return nextCityId;
// 		}
// 	}
// };


///////////////////////////////////////////////////////////////
// UPDATE PHEROMONE MATRICIES
///////////////////////////////////////////////////////////////
void updatePheromones(Ant** ants, int** distances, double** pheromones, int numCities) {

	//evaperation
	for (int i = 0; i < numCities; i++) {
		for (int j = 0; j < i ; j++) {
			pheromones[i][j] *= (1 - RHO);
			pheromones[j][i] = pheromones[i][j];
		}
	}

	// Go over each ant, look at their tour, add add pheromones to those edges
	for (int k = 0; k < numCities; k++) {
		//Loop over the ant's tour path and find the edge to update
		for (int j = 0; j < ants[k]->tour.size() - 1; j++) {
			int fromCityId = ants[k]->tour[j];
			int toCityId = ants[k]->tour[j + 1];

			int distance = distances[fromCityId][toCityId];
			pheromones[fromCityId][toCityId] += Q / (double)distance;
			pheromones[toCityId][fromCityId] = pheromones[fromCityId][toCityId];
		}
	}	
}


//https://stackoverflow.com/questions/25829143/trim-whitespace-from-a-string
string trimLeadingWhiteSpace(const string& str)
{
    size_t first = str.find_first_not_of(' ');
    if (string::npos == first)
    {
        return str;
    }
    return str.substr(first, (str.length() - first + 1));
}


// https://stackoverflow.com/questions/5891610/how-to-remove-certain-characters-from-a-string-in-c
void removeTabs(std::string &x) {
  auto it = std::remove_if(std::begin(x),std::end(x),[](char c){return (c == '\t');});
  x.erase(it, std::end(x));
}


int main(int argc, char *argv[]) {
	char *fileName = argv[1];
	srand((unsigned)time(NULL)); 
	
///////////////////////////////////////////////////////////////
// READ FROM A FILE
///////////////////////////////////////////////////////////////
	ifstream file;
	string line;
	int numCities = 0;

	file.open(fileName);
	if (file.is_open()) {
		// size the array
		while(getline(file, line)) {
			numCities += 1;
		}
	}
	file.close();

	vector<City> cities;
	cities.reserve(numCities);
	
	file.open(fileName);
	if (file.is_open()) {
		// Fill our city array
		while(getline(file, line)) {
			line = trimLeadingWhiteSpace(line);
			int spacePos = line.find_first_of(" ");
			string cityId = line.substr(0, spacePos);

			string secondPart = trimLeadingWhiteSpace(line.substr(cityId.length(), line.length() - cityId.length() + 1));
			spacePos = secondPart.find_first_of(" ");
			string x = secondPart.substr(0, spacePos);

			string thirdPart = trimLeadingWhiteSpace(secondPart.substr(cityId.length(), line.length() - cityId.length() + 1));
			spacePos = thirdPart.find_first_of(" ");
			string y = thirdPart.substr(spacePos+1);

			cities.push_back(City(stoi(cityId), stoi(x), stoi(y)));
		}
	}

	cout << "Done reading txt. cityNum = "<< numCities << endl;

///////////////////////////////////////////////////////////////
// INITIALIZE DISTANCE AND PHEROMONE MATRICIES
///////////////////////////////////////////////////////////////
	int** distances = new int*[numCities];
	for (int i = 0; i < numCities; i++)
		distances[i] = new int[numCities];
	double** pheromones = new double*[numCities];
	for (int i = 0; i < numCities; i++)
		pheromones[i] = new double[numCities];
	
	for (int i = 0; i < numCities; i++) {
		for (int j = 0; j <= i; j++) {
			double temp = pow(cities[j].x - cities[i].x, 2) +
					pow(cities[j].y - cities[i].y, 2);
			int distance = (int)sqrt(temp);
			if (distance == 0) {
				distance = MIN_DIST;
			}
			
			distances[i][j] = distance;
			distances[j][i] = distance;

			pheromones[i][j] = MIN_PHER;
			pheromones[j][i] = MIN_PHER;
		}
	}

	cout << "Done building distances and pheromones " << endl;


///////////////////////////////////////////////////////////////
// ALGORITHM
///////////////////////////////////////////////////////////////
	
	int bestTourLength = numeric_limits<int>::max();

	for (int iteration = 0; iteration < NUM_ITER; iteration++) {
		cout << "Iteration " << iteration << endl;
		Ant** ants = new Ant*[numCities];
		for (int i = 0; i < numCities; i++) {
			// Place an ant at this city
			ants[i] = new Ant(i, numCities);

			cout << "Ant " << i << " completed his tour" << endl;
			// Let ant complete its tour
			while (ants[i]->numUnvisitedCities >= 0) {
				ants[i]->moveToNextCity(distances, pheromones);
			}

			// Update the best tour
			if (ants[i]->tourLength < bestTourLength) {
				bestTourLength = ants[i]->tourLength;
				cout << "ants[" << i << "] found a new bestTourLength = " << bestTourLength << endl;
			}
		} // Ants are finished with their tours

		updatePheromones(ants, distances, pheromones, numCities);

		for (int k = 0; k < numCities; k++) {
			delete ants[k];
		}
		delete[] ants; // Ants are evil
	}
///////////////////////////////////////////////////////////////
// DEALLOCATION 
///////////////////////////////////////////////////////////////

	for (int i = 0; i < numCities; ++i) {
		delete [] distances[i];
		delete [] pheromones[i];
	}
	delete [] distances;
	delete [] pheromones;

	cout << "Done" << endl;
	return 0;
}