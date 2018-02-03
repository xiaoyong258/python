#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_

import sys,time
def timer(func):
	def deco():
		start_time=time.time()
		func()
		stop_time=time.time()
		print("The func run time is %s" %(stop_time-start_time))
	return deco
@timer
def test1():
	print("Test 1")

@timer
def test2():
	print("Test 2")

test1()

test2()
