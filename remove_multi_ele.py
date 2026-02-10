l1=[1,2,34,5,2,4435]
l2=[2,5,1]
for v1 in l2:
    while v1 in l1:
        l1.remove(v1)
print(l1)


#another method
res=[v for v in l1 if v not in l2]
print(res)




#rmeoving tuples in list
l3=[(1,2),(),(3,4),(7,8),(5,6),(10,)]
l4=[t for t in l3 if t]
l7=[]
l1=[1,1,2,4,3,2,22,2,2,4,5,17,4,4,4,5,5,5,66,66,32]
print(l1)
for i in range(len(l1)):
    count=0
    val=l1[i]
    for x in range(len(l1)):
        if val == l1[x]:
            count+=1
    if count>=2:
        print("element ",val, "is repeated",count,"times")
        l7.append(val)
print(l7)
l8=set(l7)
print(l8)

