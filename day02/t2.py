#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_

import sys

names = ['Alex',"Tenglan",'Eric',"Rain","Tom","Amy"]
print(names[1:4])
print(names[1:-1])
print(names[0:3])
print(names[:3])
print(names[3:-1])
print(names[0::2])
print(names[::2])

names.append("我是新来的")
print(names)

names.insert(2,"强行从Eric前面插入")
print(names)

names.insert(5,"从Eric后面插入新姿式")
print(names)

names[2] = "该换人了"
print(names)

del names[2]
print(names)

del names[4]
print(names)

names.remove("Eric")
print(names)

names.pop()
print(names)
b = [1,2,3]

names.extend(b)
print(names)

name_copy = names.copy()
print(name_copy)

names.insert(5,"Amy")
print(names.count("Amy"))

names[-3] = '3'
names[-2] = '2'
names[-1] = '1'

names.sort()
print(names)

print(names.index("Amy"))
