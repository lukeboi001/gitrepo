#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  euklides_nwd.py

def nwd_klasyczna(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def main(args):
    a = int(input("Podaj liczbę 1: "))
    b = int(input("Podaj liczbę 2: "))
    print("NWW({}, {}) = {}".format(a, b, nwd_klasyczna(a, b)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
