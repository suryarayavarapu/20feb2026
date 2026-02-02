#working with list constructor
# items1=list((1,55,32,462,64))
#print(items1)
#items2=list(input("enter values"))
#print(items2)
#items3=list((input("enter values")))
#print(items3) 
#using mapping
#list3=list(map(int,input("enter values seperated by space").split()))
#print(list3)
# using list comprehension
#list4=[int(x) for x in input("enter values for making list").split()]
#print(list4)
#a=[2]*5
#b=[3,5]*3
#print(a,"\n",b)



var1=[]
var1.append(5)
print(var1)
print(var1.insert(0,10))# this is wrong way insert is method you can apply but  it returns none, we required modified can be get through below syntax
var1.insert(0,34)#insert 0 th index calues is 34
print (var1)
#var1.extend(45,65)#if i want to add list, extend take single arguments but i gave 2 its type error
var1.extend([45,65])#it will extend
print(var1)