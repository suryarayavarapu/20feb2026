# append and extend in list
a=[3,4,5,6]
a.append([43,53,2])
a.extend([4,5,3])
print(a)

from itertools import chain
m=[33,23,443]
a.extend(chain(m))
print(a)

#delete , remove, index based deleting
#if  element found in list remove
a.remove(5)
a.append(5)
a.extend([3,5,4,5])
print(a)# it remove first occurnce element founded
# to remove all elements which having 5 in a list using for loop is wrong because index can skip, to avoid this use while loop
find=5
find=int (find)
#for f in range(len(a)):
 #   if find==a[f]:
#        a.remove(find)
#print(a)
#using while loop removing finded element in all list
while find in a:
    a.remove(find)
print(a)