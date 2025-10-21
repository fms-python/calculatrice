#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Calculatrice à 4 opérations
"""


def add(op1, op2):
    return op1 + op2


def substract(op1, op2):
    return op1 - op2


def multiply(op1, op2):
    return op1 * op2


def divide(op1, op2):
    return op1 / op2


if __name__ == '__main__':
    print(add(2, 3))
    print(add(3, 2))
    print(substract(5, 2))
    print(substract(2, 5))
    print(multiply(3, 5))
    print(multiply(5, 3))
    print(divide(6, 3))
    print(divide(3, 6))
