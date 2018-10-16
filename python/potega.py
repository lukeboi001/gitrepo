#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  Obliczanie potęgi podstawy podniesionej do wykładnika


def potega_it(a, n):
    wynik = 1
    for i in range(n):
        wynik = wynik * a
        print(wynik)
        
    return wynik
    
def main(args):
    #a, n = 3, 4
    #print("Potęga {} do {} wynosi {}".format(a, n, potega_it(a, n)))
    assert(potega_it(0, 2) == 0)
    assert(potega_it(1, 2) == 1)
    assert(potega_it(2, 2) == 4)
    assert(potega_it(4, 2) == 16)
    
    
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
