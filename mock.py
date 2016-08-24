# This is a Mock project for DevOps class

# Python-Paramiko (Module)
# SSH client online
# Python-OS (Module)	- create directory
# 	


import paramiko
import cmd


ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.13', username='ahsan', password='ahsankhan')
stdin, stdout, stderr = ssh.exec_command("uname -a && /sbin/ifconfig -a | grep 192.168.0")
print stdout.read()