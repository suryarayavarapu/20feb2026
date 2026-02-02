i=0
list1=[]
listx=input("enter numbers by white space")
listy=listx.split(" ")
for i in range (len(listy)):
    z=int(listy[i])
    list1.append(z)
print(list1)
n=len(list1)
list2=[]
target=int(input("enter value which 2 numbers added and gives sum"))
#target=int(input("enter target to meet add of two elements in list"))
for i in range (n-1):
    for j in range(i+1,n):
        sum1=list1[i]+list1[j]
        if sum1==target:
            list2.append(i)
            list2.append(j)
            break
    print("\n")
print(list2)
#after 6 th line if i provide j=i+1 next for loop start at j=0 , but i need jth indices is i+1 better to write line 7
