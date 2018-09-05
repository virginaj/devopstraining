#!/bin/bash -x

#webservers
ansible -m shell -a "sudo yum install -y httpd" -i inventory/ansible-nodes webservers

ansible -m copy -a "src=/httpd.conf dest=~/test" -i inventory/ansible-nodes webservers --become

ansible -m service -a "name=nginx state=started enabled=yes" inventory/ansible-nodes --become

#dbservers
ansible -m shell -a "sudo yum install -y mariadb-server" -i inventory/ansible-nodes dbservers