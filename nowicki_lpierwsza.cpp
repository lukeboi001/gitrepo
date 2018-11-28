/*
 * nowicki_lpierwsza.cpp
 */


#include <iostream>
using namespace std;

int liczbapierwsza(int n)
{
	if(n<2)
		return false;
	for(int i=2; i * i<=n; i++)
		if(n % i == 0)
			return false;
	return true;
}

int main(int argc, char **argv)
{
	int n;
	cout << "Podaj liczbę pierwszą: ";
	cin >> n;
	if(liczbapierwsza(n))
		cout << "Liczba jest pierwsza" << endl;
	else
		cout << "Błąd, liczba nie jest pierwsza" << endl;
	return 0;
}

