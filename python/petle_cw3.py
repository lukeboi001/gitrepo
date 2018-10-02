#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petle_cw2.py
#  
#  


def main(args):
    m = int(input("Podaj liczbę: "))
    while m < 1:
        print("Błędne dane!")
        m = int(input("Podaj liczbę: "))
    
    for liczba in range(m+1):
        print(liczba**2, " ", end=" ")

    return 0
  
if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
