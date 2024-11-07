#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python program showing
# abstract base class work

from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 6 sides")


class Quadrilateral(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 4 sides")


def main():
    # Driver code
    R = Triangle()
    R.noofsides()
    K = Quadrilateral()
    K.noofsides()
    R = Pentagon()
    R.noofsides()
    K = Hexagon()
    K.noofsides()


if __name__ == '__main__':
    main()