run: runants.o
	g++ -o run runants.o -lm -fopenmp


runants.o: runants.cpp city.h parameters.h ant.h
	g++ -c -g -std=c++11 runants.cpp city.h parameters.h ant.h -lm -fopenmp
	
clean:
	rm *.o -f
	rm *.gch -f
	rm a.out -f
	rm runants -f