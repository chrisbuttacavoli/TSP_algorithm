#include <iostream>

using namespace std;

class City {
public:
	int id;
	int x;
	int y;

	City(int Id, int xcoord, int ycoord) {
		this->id = Id;
		this->x = xcoord;
		this->y = ycoord;
	}
	
	void stuff() { cout << "BOB" << endl; }

};