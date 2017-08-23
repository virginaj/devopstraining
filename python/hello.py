#!/usr/bin/python 


def foo():
	f = open('/var/log/kern.log')
	lines = f.readlines()
	for line in lines:
		print int(line.split()[2].split(':')[2]) * 10
		


def hello_function():
	print("Hello World!")

def variable_function(myvar):
	var1 = "test"
	print( var1 + myvar)
	return var1

hello_function()
var1 = variable_function("working")
print(var1)