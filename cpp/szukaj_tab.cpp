/*
 * szukaj_tab.cpp
 */


#include <iostream>
using namespace std;


int szukaj(int tab, int x, int n) {
    for (int i = 0; i < n; i++) {
        if (tab[i] == x)
            return i;
        }
        return -1;
    }


int main(int argc, char **argv)
{
    int n = 10;
	int tab[n] = {12, 11, 8, 6, 8, 4, 10, 5, 2, 3};
    int x = 0;
    cout << "Podaj liczbę: ";
    cin >> x;
    int indeks = szukaj(tab, x, n);
    if (indeks(tab, x) > -1)
        cout << "Znaleziono";
    else
        cout << "Nie znaleziono";
	return 0;
}

