#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_

import sys

def foo():
	print('in the foo')
	def bar():
		print('in the bar')
	bar()
foo()

