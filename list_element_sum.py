list1=[234,3334,13,445]
list2=[]
for i in range(len(list1)):
    s=0
    x=i
    while list1[x]>0:
        s=s+list1[x]%10
        list1[x]=list1[x]//10
    list2.append(s)
print(list2)
list1=[2345,33345,135,5445]
#using list comprehension
list3=[sum(int(digit) for digit in str(f)) for f in list1]
print(list3)


list1=[245,3345,15,55]
#using lambda, map
l6=list(map(lambda f: sum(int(digit) for digit in str(f)),list1))
print(l6)


#using sum and map
list7=[532,345,346,2323]
res=[sum(map(int, str(value))) for value in list7]
print(res)
