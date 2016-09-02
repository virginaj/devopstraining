#!/usr/bin/python
def loop_func(count=None):
	if count == None:
		print('Count is None')
		count =5
	for i in range(count):
		print(i)
loop_func()
