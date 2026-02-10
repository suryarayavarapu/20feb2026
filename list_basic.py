a=int(input(" enter a value"))
b=int(input(" enter b value"))
print(type(a))
if a>b:
    print("max of two numbers a,b is a",a)
else:
    print("max of two numbers a,b is  b",b)


#using max function
print("max values are",max(a,b))


#using list compreshension
print(a if a>b else b)


#using sort
list1=input("enter values by space it will take into string")
list1=list1.split(" ")
arr=[]
print(list1)
for i in range(len(list1)):
    list1[i]=int (list1[i])
    arr.append(list1[i])
arr.sort()
print(arr)