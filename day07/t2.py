#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_

import sys

class Dog(object):
    name = "我是类变量"

    def __init__(self,name):
        self.name = name

    @staticmethod
    def eat():
        print("I'm is eating" )

    @classmethod
    def drink(self):
        print("%s is drinking" %self.name)

    @property
    def smile(self):
        print("%s is smiling" %self.name)

d = Dog("ChenRonghua")
d.eat()
d.drink()
d.smile

print(d.__doc__)
#print(d.___module__)
print(d.__class__)
