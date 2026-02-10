l1=[2,5,3,1,4,9,13,0]
l2=[]
max=l1[0]
x=2
while x>0:
    for i in range(len(l1)-1):
        if max>l1[i+1]:
            max=max
        else:
            max=l1[i+1]
    x-=1
print(max)
if max in l1:
    l1.remove(max)
print(l1)
max=l1[0]
for i in range(len(l1)-1):
    if max>l1[i+1]:
        max=max
    else:
        max=l1[i+1]
print(max)





#simplest form for 2nd element largest
l3=[2,5,3,1,4,10,15,0]
x=2
while x>0:
    max=l3[0]
    for i in range(len(l3)-1):
        if max>l3[i+1]:
            max=max
        else:
            max=l3[i+1]
    print(max)
    l3.remove(max)
    print(l3)
    x-=1
print(max)

