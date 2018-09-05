

## Test Ad hoc commands and ssh command comparison

ssh ansible-node "hostname -f"
ansible ansible-node   -a "hostname -f"

ssh ansible-node "mkdir /home/ec2-user/mytestdir"
ansible ansible-node  -a "mkdir /home/ec2-user/testdirAnsible"
ansible ansible-node -m copy -a "src=inventory/ansible-nodes dest=/tmp/ansible-nodes"
ansible ansible-node -a "cat /tmp/ansible-nodes" 
ansible ansible-node -b -m yum -a "name=httpd state=present"
ansible ansible-node -b -m yum -a "name=git state=present"
ansible ansible-node -b -m git -a "repo=https://github.com/becloudready/prometheus_monitoring.git dest=/tmp version=HEAD"

# Using Ansible modules in ad-hoc commands


ansible -m file -a "path=/home/ec2-user/usingAnsible state=directory" ansible-node --become
ansible -m copy -a "src=Vagrantfile dest=/tmp" ansible-node --become

