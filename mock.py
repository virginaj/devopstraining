# This is a Mock project for DevOps class

# Python-Paramiko (Module)
# SSH client online
# Python-OS (Module)	- create directory
# 	


import paramiko
import cmd



def clt():
	l=['localhost']
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect( 'l' , username='ahsan', password='ahsankhan')
	ins, out, err = ssh.exec_command("uname -a && /sbin/ifconfig -a | grep 192.168.0")
	ab=out.read()
	print ab.split('\n')

	for line in ab.split('\n\n'):
		print ('\n')
clt()