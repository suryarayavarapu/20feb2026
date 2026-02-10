list1=input("enter values by space it will take into string")
list1=list1.split(" ")
arr=[]
print(list1)
for i in range(len(list1)):
    list1[i]=int (list1[i])
    arr.append(list1[i])
print(arr)
for i in range (len(arr)):
    print(arr[i], end=" ")