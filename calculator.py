#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Calculatrice
"""


def add(op1, op2):
    return op1 + op2


def substract(op1, op2):
    return op1 - op2


if __name__ == '__main__':
    assert add(2, 3) == 5
    assert add(5, 2) == 7
    assert substract(2, 5) == -3
