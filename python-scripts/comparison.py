#!/usr/bin/python
i=5
if i == 4:
	print('match')
else:
	print('No Match')
s = " This is a test"
if s == " This is a test":
	print("Match")
else:
	print("Failed to match")
l = [1,2,3,4,5,6,6,76,7]
if l == [1,2,3,4,5,6,6,76,7]: 
	print('***found IT ***')
else:
	print ('Not Found')
def foo():
	return[11,22,33,44]
if 99 in foo():
	print('GOOD')
else:
	print('No Good')
s="1"
t=1
if s==t:
	print("Match")
else:
	print("Mismatch")

