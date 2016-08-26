# This is a Mock project for DevOps class

# Python-Paramiko (Module)
# SSH client online
# Python-OS (Module)	- create directory
# 	


import paramiko
import requests



def clt():
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect( '192.168.0.13' , username='ahsan', password='ahsankhan')
	ins, out, err = ssh.exec_command("mkdir /opt/google ; cd /opt/google && wget http://www.google.com" )
	
	
clt()