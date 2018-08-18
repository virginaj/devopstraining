

## Test Ad hoc commands and ssh command comparison

ssh ansible-node "hostname -f"
ansible ansible-node  -i inventory/ansible-nodes -a "hostname -f"

ssh ansible-node "mkdir /home/ec2-user/mytestdir"
ansible ansible-node  -i inventory/ansible-nodes -a "mkdir /home/ec2-user/testdirAnsible"



ansible ansible-node -i inventory/ansible-nodes -m copy -a "src=inventory/ansible-nodes dest=/tmp/ansible-nodes"


ansible ansible-node -i inventory/ansible-nodes -a "cat /tmp/ansible-nodes" 

ansible ansible-node -i inventory/ansible-nodes -b -m yum -a "name=httpd state=present"

ansible ansible-node -i inventory/ansible-nodes -b -m yum -a "name=git state=present"

ansible ansible-node -i inventory/ansible-nodes -b -m git -a "repo=https://github.com/becloudready/prometheus_monitoring.git dest=/tmp version=HEAD"
