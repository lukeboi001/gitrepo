#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  bez nazwy.py
#  


def main(args):
    
    n = int(input("Podaj n: "))
    m = int(input("Podaj m: "))
    for liczba in range(n, m + 1):
        print (liczba, " ", end="")
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
