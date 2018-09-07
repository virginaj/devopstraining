#!/usr/bin/python

f = open("N4xFilterTier1.csv")

#mylines =f.read()

mylines= f.readlines()

#print mylines

ll =[]

for line in mylines[1:]:
    if float(line.split(',')[0]) > 4.0:
        #print line
        ll.append(line)


print ll

f = open ('output', 'w')
for l in ll:
    f.write(str(l))



