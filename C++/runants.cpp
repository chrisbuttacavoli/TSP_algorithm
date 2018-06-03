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
//#include "Ant.h"

#define ALPHA 2.0
#define BETA 0.5
#define Q 1
#define RHO 0.6
#define MIN_DIST 1
#define MIN_PHER 0.1
#define NUM_ITER 30

using namespace std;

class Tour {
	int tourLength = 0;
	vector<int> path;
};


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
		//cout << "next city id = " << nextCityId << endl;

		// Update the ant's tour
		tourLength += distances[prevCityId][nextCityId];
		tour.push_back(false);
	
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
				//cout << "Unvisited city: " << cityId << endl;
				nij = 1 / (double) distances[currentCityId][cityId];
				Tij = 1 / pheromones[currentCityId][cityId];
				//cout << "nij = " << nij << " Tij = " << Tij << " (i = "<< currentCityId << " j = "<< cityId
				//	<< " distance = "<<distances[currentCityId][cityId] <<")"<<endl;
				temp = pow(nij, ALPHA)*pow(Tij, BETA);
				probabilities.push_back(temp);
				denominator += temp;
			}
			else {
				probabilities.push_back(0);
			}
		}

		//cout << "denominator = " << denominator << endl;

		// compute the probability for each city
		for (int cityId = 0; cityId < numCities; cityId++) {
			if (unvisitedCities[cityId] == true)
				probabilities[cityId] = probabilities[cityId] / denominator;
			else
				probabilities[cityId] = 0;
			//cout << probabilities[cityId] << endl;
		}

		return probabilities;
	}

	
	int _selectNextCityId(vector<double> p){
		//srand((unsigned)time(NULL));
		//srand(5);
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
		//elect the next city based on probabilities
			int nextCityId = _selectNextCityId(_computeProbability(currentCityId,distances,pheromones));
			return nextCityId;
		}
	}


};


///////////////////////////////////////////////////////////////
// UPDATE PHEROMONE MATRICIES
///////////////////////////////////////////////////////////////
void updatePheromones(Ant** ants, int** distances, double** pheromones, int numCities) {

	//evaperation
	for (int i = 0; i < numCities; i++) {
		for (int j = 0; j <= i ; j++) {
			pheromones[i][j] *= (1 - RHO);
			pheromones[j][i] *= (1 - RHO);
		}
	}


	//add pheromone
	int tourSize = numCities + 1;
	
	// Go over each ant, look at their tour, add add pheromones to those edges
	for (int i = 0; i < numCities; i++) {
		//Loop over the ant's tour path and find the edge to update
		for (int j = 0; j < numCities; j++) {
			int fromCityId = ants[i]->tour[j];
			int toCityId = ants[i]->tour[j + 1];

			int distance = distances[fromCityId][toCityId];
			//cout << "Q / (double)distance" << endl;
			pheromones[fromCityId][toCityId] += Q / (double)distance;
			pheromones[toCityId][fromCityId] += Q / (double)distance;
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
			// NEED POW
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

	cout << "Done building distances and pheroomones " << endl;


///////////////////////////////////////////////////////////////
// ALGORITHM
///////////////////////////////////////////////////////////////
	
	int bestTourLength = numeric_limits<int>::max();

	for (int iteration = 0; iteration < NUM_ITER; iteration++) {
		Ant** ants = new Ant*[numCities];

		cout << "Iteration " << iteration << ")" << endl;
		for (int i = 0; i < numCities; i++) {
			ants[i] = new Ant(i, numCities);

			while (ants[i]->numUnvisitedCities >= 0) {
				ants[i]->moveToNextCity(distances, pheromones);
			}

			if (ants[i]->tourLength < bestTourLength) {
				bestTourLength = ants[i]->tourLength;
				cout << "ants[" << i << "] found a new bestTourLength = " << bestTourLength << endl;
			}

		}
		/*
		for (int k = 0; k < numCities; k++) {
			for (int h = 0; h < numCities; h++) {
				cout << pheromones[k][h] << " ";
			}
			cout << endl;
		}
		*/
		
		updatePheromones(ants, distances, pheromones, numCities);

		for (int k = 0; k < numCities; k++) {
			delete ants[k];
		}
		delete[] ants;
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