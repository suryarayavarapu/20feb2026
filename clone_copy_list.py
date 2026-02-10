l1=[2,3,4,5,6]
l2=l1.copy()
print(l2)

#by list sclicing
l3=l1[:]
print(l3)

#using lsit constructor
l4=list(l3)
print(l4)

list5=[l4[i] for i in range(len(l4))]
print("\n",list5)

import copy
a=[[1,3],[4,5],[5.,7]]
b=copy.deepcopy(a)
print(b)