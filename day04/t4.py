#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_

import sys

def bar():
	print('in the bar')
def foo():
	print('in the foo')
	bar()
foo()
	
