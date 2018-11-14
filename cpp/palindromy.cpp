/*
 * znaki.cpp
 */


#include <iostream>
#include <string.h>

using namespace std;

bool palindrom(

int main(int argc, char **argv)
{
    const int rozmiar = 20;
    char wyraz[20] = "ryba";
    cout << "Podaj wyraz lub zdanie: ";
    cin.getline(wyraz, rozmiar);
    cout << cin.gcount() << endl;
    cout << strlen(wyraz) << endl;
    if (palindrom(wyraz, strlen(wyraz)))
        cout << "Palindrom!";
    else
        cout << "Nie palindrom";
    return 0;
}

