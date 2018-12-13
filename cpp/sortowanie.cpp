/*
 * sortowanie.cpp
 */


#include <iostream>
#include <cstdlib>
using namespace std;

void wypelnij(int tab[], int roz) {
    srand(time(NULL));  //inicjacja generatora liczb pseudolosowych
    cout << "Wprowadź " << roz << " liczb: " << endl;
    for(int i=0; i<roz; i++) {
        tab[i] = rand() % 101;  // liczby od 0 do 100
    }
}

void drukuj(int tab[], int roz) {
    for(int i=0; i<roz; i++) {
        cout << tab[i] << " ";
        }
}

void zamien1(int a, int b) {
    cout << a << " " << b << endl;
    int tmp = a;
    a = b;
    b = tmp;
    cout << a << " " << b << endl;
    
}


void sort_bubble(int tab[], int n) {
    for (int j = n-1; j > 0; j--) {
        for (int i = 0; i < j; i++) {
            if (tab[i] > tab[i+1])
                zamien1(tab[i], tab[i+1]);
        }
    }
    
}




int main(int argc, char **argv)
{
	int roz = 20;
    int tab[roz];
    wypelnij(tab, roz);
    drukuj(tab, roz);
    cout << endl << endl;
    // sort_bubble(tab, roz);
    zamien1(5, 10);
    cout << endl;
	return 0;
}

