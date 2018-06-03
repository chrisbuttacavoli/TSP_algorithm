#include <fstream>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>

#include "city.h"

#define ALPHA 2
#define BETA 0.5
#define Q 1
#define RHO 0.6
#define MIN_DIST 1
#define MIN_PHER 0.1

using namespace std;


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


// vector<City> ReadCityData(char* fileName) {
// 	ifstream file;
// 	string line;
// 	int numCities = 0;

// 	file.open(fileName);
// 	if (file.is_open()) {
// 		// size the array
// 		while(getline(file, line)) {
// 			numCities += 1;
// 		}
// 	}
// 	file.close();

// 	// City cities[numCities];
// 	vector<City> cities;
// 	cities.reserve(numCities);
	
// 	file.open(fileName);
// 	if (file.is_open()) {
// 		// Fill our city array
// 		while(getline(file, line)) {
// 			line = trim(line);
// 			int firstSpacePos = line.find(" ");
// 			int secondSpacePos = line.find(" ", firstSpacePos + 1);
// 			int endLine = line.find("\n", secondSpacePos + 1);

// 			int cityId = stoi(line.substr(0, firstSpacePos));
// 			int x = stoi(line.substr(firstSpacePos, secondSpacePos));
// 			int y = stoi(line.substr(secondSpacePos, endLine));

// 			cities.push_back(City(cityId, x, y));
// 		}
// 	}
// 	return cities;
// }


int main(int argc, char *argv[]) {
	char *fileName = argv[1];
	
	
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
			string y = thirdPart.substr(0, spacePos);

			// int secondSpacePos = (secondPart).find(" ", firstSpacePos + 1);
			// int endLinePos = line.find("\n", secondSpacePos + 1);

			// cout << line << endl << firstSpacePos << " " << secondSpacePos << " " << endLine << endl;
			// cout << line.substr(0, firstSpacePos) << endl;
			// int cityId = stoi(line.substr(0, firstSpacePos));
			// int x = stoi(line.substr(firstSpacePos, secondSpacePos - firstSpacePos + 1));
			// int y = stoi(line.substr(secondSpacePos, endLine - secondSpacePos + 1));
			
			// string x = line.substr(firstSpacePos, secondSpacePos - firstSpacePos);
			// string y = line.substr(secondSpacePos, endLinePos - secondSpacePos);
			// cout << line << endl << "  " << firstSpacePos << " " << secondSpacePos << endl;
			// cout << "Here: " << cityId << " " << x << " " << y << endl;
			// for (int i = 0; i < line.length(); i++)
			// 	cout << (int)line[i] << " " << endl;

			// cout << line << endl;
			// cout << "GO: " << cityId << " " << x << " " << y << endl;
			cities.push_back(City(stoi(cityId), stoi(x), stoi(y)));
		}
	}

///////////////////////////////////////////////////////////////
// INITIALIZE DISTANCE AND PHEROMONE MATRICIES
///////////////////////////////////////////////////////////////
	int** distances = new int*[numCities];
	for (int i = 0; i < numCities; i++)
		distances[i] = new int[numCities];
	double** pheromones = new double*[numCities];
	for (int i = 0; i < numCities; i++)
		pheromones[i] = new double[numCities];
	
	// double pheromones[numCities][numCities];
	for (int i = 0; i < numCities; i++) {
		for (int j = 0; j < i; j++) {
			// NEED POW
			double temp = pow(cities[j].x - cities[i].x, 2) +
					pow(cities[j].y - cities[j].y, 2);
			int distance = (int)sqrt(temp);
			if (distance = 0) {
				distance = MIN_DIST;
			}

			distances[i][j] = distance;
			distances[j][i] = distance;
			pheromones[i][j] = MIN_PHER;
			pheromones[j][i] = MIN_PHER;
		}
	}


///////////////////////////////////////////////////////////////
// 
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