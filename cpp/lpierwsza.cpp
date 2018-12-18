/*
 * lpierwsza.cpp
 */


#include <iostream>
using namespace std;
int main(int argc, char **argv)
{
	int n = 0;
    cout << "Podaj liczbę: ";
    cin >> n;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            cout << "Liczba złożona";
            return 0;
            }
        }
    cout << "liczba pierwsza";
	return 0;
}

