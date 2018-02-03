#!/usr/bin/python3.5
# _*_ coding: utf-8 _*_

import sys

user,passwd='Alex','abc123'

def auth(func):
	def wrapper(*args,**kwargs):
		username = input("Username:").strip()
		password = input("Password:").strip()
		if user == username and passwd == password:
			print("\033[32:1mUser has passed authentication!\033[0m")
			res = func(*argv,**kwargs)
			print("After authentication")
			return res
		else:
			exit("\033[31:1mInvalid username or password!\033[0m")
	return wrapper


def index():
	print("Welcome to index page")
@auth
def home():
	print("Welcome to home page")

def bbs():
	print("Welcome to bbs page")

index()
home()
bbs()
