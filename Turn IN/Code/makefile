run: runants.o
	g++ -g -std=c++11 -o run runants.o


runants.o: runants.cpp city.h parameters.h ant.h
	g++ -c -g -std=c++11 runants.cpp city.h parameters.h ant.h
	
clean:
	rm *.o -f
	rm *.gch -f
	rm a.out -f
	rm runants -f
	rm run -f