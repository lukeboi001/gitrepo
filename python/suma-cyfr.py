#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  suma-cyfr.py

def sumuj_cyfry(liczba):
    suma = 0
    while liczba >0:
        suma = suma + (liczba % 10)
        liczba = int(liczba / 10)
    return suma

def main(args):
    liczba = int(input("Podaj liczbę minimum dwucyfrową: "))
    while liczba < 10:
        print("Błąd!")
        liczba = int(input("Podaj liczbę minimum dwucyfrową: "))
   
    print("Suma:", sumuj_cyfry(liczba))
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
