#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  szablon.py

# int() - przekształca argument na liczbę całkowitą
# czyli typ INTEGER

def hello():
    print("Witaj w Python!")
    
def witaj():
    imie = input("Jak masz na imię?")
    print ("Witaj", imie,"!")
    
def suma(l1, l2):
    print("Suma:", l1+l2)

def suma2(a, b):
    """
    Funkcja sumuje dwie liczby i zwraca wynik
    """
    return a + b
    
def roznica(l1, l2):
    print("Różnica:", l1-l2)
    
def iloczyn(l1, l2):
    print("Iloczyn:", l1*l2)
    
def iloraz(l1, l2):
    print("Iloraz:", l1/l2)
        
def main(args):
    # zmienne lokalne, o zasięgu lokalnym
    a = int(input("Podaj 1. liczbę: "))
    print (a)
    b = int(input ("Podaj 2. liczbę: "))
    print (b)
    
    print("Suma:", suma2(a, b))
    # suma(a, b)
    # print("Różnica:", a - b)
    roznica(a, b)
    # print("Iloczyn:", a * b)
    iloczyn(a, b) 
    # print("Iloraz:", a / b)
    iloraz(a, b) 
    
    hello()  # wywolanie funkcji
    witaj()
    
    return 0
    
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
