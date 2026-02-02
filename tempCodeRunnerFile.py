n=int(input("enter numbers count in list"))
i=0
list1=[]
list2=[]
while i<n:
    x=int(input("enter integer values"))
    list1.append(x)
    i+=1
print(list1)
target=int(input("enter target to meet add of two elements in list"))
for i in range (n):
    if target==list1[i]+list1[i+1]:
        print(list2.append(i))
print(list2)