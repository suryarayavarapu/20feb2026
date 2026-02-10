l1=[2,42,5,3,55,66,23,62]
l2=[]
l3=[]
l4=[]
l5=[]
#even count
count =0
for l in range(len(l1)):
    if l1[l]%2==0:
        l2.append(l1[l])
print(l2)


for value in l1:
    if value%2==0:
        count+=1
        l3.append(value)
print(l3)
print(count)


l4=[element for element in l1 if element%2==0]
print(l4)

l5=[v for v in l1 if v & 1==0]
print(l5)


