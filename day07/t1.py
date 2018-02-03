#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_

import sys

class A:
    def __init__(self):
        self.n = 'A'

class B:
    pass

class C(A):
    def __init__(self):
        self.n = 'C'

class D(B,C):
        pass

obj = D()

print(obj.n)

