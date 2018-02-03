#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_

import sys

def bar():
	print("in the bar")
def test2(func):
	print(func)
	return(func)

print(test2(bar))
bar1=test2(bar)
bar1()
