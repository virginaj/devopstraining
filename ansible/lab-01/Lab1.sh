#!/bin/bash -x
#weka.csv

echo -n "Enter file name: " 
read name

if [ -e "$name" ]; then
	echo "Yes, file is exists"

	ansible -m copy -a "src=~/Downloads/$name dest=~/test" node02 --become
	#ansible -m copy -a "src=~/Downloads/$name dest=~/test" node03 --become

else
	echo "No, file is not exists"
fi

# had issue with if statement