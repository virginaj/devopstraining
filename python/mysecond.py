#!/usr/bin/python



thisdict =	{
   "name": 'VJ',
   "city": 'MG',
   "name1": 'Tajes',
   "city1": 'Northbrook'
}


for x, y in thisdict.items():
    print(x, y)

for k,v in thisdict.items():
    print "{}: {}".format(k,v)


l1 = ['v','c','t','f']
l2 = ['MortonGrove','Virgina','Northbrook','Niles']

dict = {[l1],[l2]}
for x, y in dict.items():
    print(x, y)

