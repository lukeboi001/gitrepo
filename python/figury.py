#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  figury.py

  

def main(args):
    
    a = int(input("Podaj 1 bok: "))
    b = int(input("Podaj 2 bok: "))
    znak = input("Podaj znak: ")
    for i in range(a):
        for j in range(b):
            print(znak, end='')
        print()
        
    print()
        
    for i in range(a):
        for j in range(b):
            if j == 0 or j == b -1:
                print(znak, end='')
            else:
                print(" ", end='')
        print()
        
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
