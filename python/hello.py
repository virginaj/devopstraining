#!/usr/bin/python 

def foo():
	f = open('/var/log/kern.log')
	lines = f.readlines()
	for line in lines:
		print int(line.split()[2].split(':')[2]) * 10
		
def parse_log_file():
	with open('/home/ec2-user/messages') as f:
		lines = f.readlines()
	
	f = open('ansible-node-log','w')

	for line in lines:
	    	f.write(line.replace('ansible-server','ansible-node'))
	f.close()


def hello_function():
	print("Hello World!")

def variable_function(myvar):
	var1 = "test"
	print( var1 + myvar)
	return var1

hello_function()
var1 = variable_function("working")
print(var1)
parse_log_file()
