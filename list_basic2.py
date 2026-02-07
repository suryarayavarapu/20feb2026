list1=[2,34,5,6,7,32]
list1[0],list1[-1]=list1[-1],list1[0] # interchnging first and 2nd eleemnt without changing remaining element #direct assignment method
print(list1)

a=list1[-1]
list1[-1]=list1[0]
list1[0]=a  #usinf 3rd variable swapping firs and last element
print(list1)

pair=list1[0],list1[-1]
list1[-1],list1[0]=pair
print(list1)


#by using [] and concatenating operator
list2=[34,45,23,64,346]
list2=[list2[-1]]+list2[1:len(list2)-1]+[list2[0]]# middle term no square brackets rest of 2 having square brackets
print(list2)


list3=[45,56,24,67,34]

#by using *operator
print("\n")
a,*b,c=list3
list3=c,*b,a
print(list3)   #tuple output i need to convert to list
print(list(list3))

print([c,*b,a]) #direct list


print(list3[-1:])
print(list3[1:len(list3)-1])
list4=list3[-1:]+list3[1:-1]+list3[:1]#this element list3[1:-1]  -1 indicates last element i.e., nth eleement you need to subtract n-1 
print(list4)


#using XOr operation
a=10
b=20
a=a^b
b=a^b
a=a^b
print(a,b)