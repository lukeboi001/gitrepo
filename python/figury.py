#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py

def prostokat1(a, b, znak):
    for i in range(a):
        for j in range(b):
            print(znak, end='')
        print()

        
def prostokat2(a, b, znak):
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b -1 or i == 0 or i == a - 1:
                print(znak, end='')
            else:
                print(" ", end='')
        print()

  
def choinka1(h, znak):
    for i in range(h):
        for i in range(h):
            if i == 0 or i == h + 1:
                print(znak, end='')
        print()
    
    

    

def main(args):
    a = int(input("Podaj 1 bok: "))
    b = int(input("Podaj 2 bok: "))
    h = int(input("Podaj wysokość: "))
    znak = input("Podaj znak: ")
    prostokat1(a, b, znak)
    print()
    prostokat2(a, b, znak)
    print()
    choinka1(h, znak)
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
