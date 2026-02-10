l1=[1,2,3]
l2=[4,5,6]
l3=l1+l2
print(l3)
l4=[7,8,9]
l3.extend(l4)
print(l3)
l5=[10,11,12]
import operator
l6=[*l4,*l5]
print(l6)
l7=[13,14,15,16]
for val in l7:
    l6.append(val)
print(l6)
#list comprehension
l8=[17,18,19]
l9=[x for x in l6] + [y for y in l8]
print(l9)