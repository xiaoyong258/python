#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_
# 多态示例: polymorphisn
import sys

class Animal(object):
    def __init__(self, name):
        self.name = name
    def talk(self):
        raise NotImplementedError("Subclas must implement abstract method")

class Cat(Animal):
    def talk(self):
        print('%s: miao miao miao!!!' %self.name )

class Dog(Animal):
    def talk(self):
        print("%s: wang wang wang!!!" %self.name)

def func(obj):
    obj.talk()

c1 = Cat('小青')
d1 = Dog('张山')

func(c1)
func(d1)

