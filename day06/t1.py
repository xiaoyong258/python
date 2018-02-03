#!/usr/bin/python3.5 
# _*_ coding: utf-8 _*_

import sys
import pdb



def person(name,age,sex,job):
    def bark(d):
        print("dog %s:wang.wang.wang..." %d['name'])
    data={
        'name':name,
        'age':age,
        'sex':sex,
        'job':job
    }
    return data

def dog(name,dog_type):
    def walk(p):
        print("person %s is walking..." %p['name'])
    data={
        'name':name,
        'type':dog_type
    }
    return data

   
d1=dog("李磊","京巴")
p1=person("严帅",36,"F","运维")
p2=person("林海峰",27,"F","Teacher")

d1.walk("hi")
