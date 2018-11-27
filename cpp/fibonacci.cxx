/*
 * fibonacci.cxx
 * 
 */


#include <iostream>
using namespace std;

long int fibonacci_it(int n) {
    long int wynik = 0;
    return wynik; 
    
}

int main(int argc, char **argv)
{
	int n;
    cout << "Podaj numer ciągu :";
    cin >> n;
    cout << "Ciąg Fibonacciego do wyrazu " << n << ":" << endl;
    cout << fibonacci_it(n);
	return 0;
}

