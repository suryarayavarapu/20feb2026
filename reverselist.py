a=[2,4,3,4,6]
a.reverse()
print(a)

#using for loop by pop method , it will empty the original list
b=[]
for i in range(len(a)):
    b.append(a.pop())
print(a)
print(b)

c=b[-1::-1]
d=b[::-1]
print(c)
print(d)


#using while loop revesring a list
b=[12,34,32,544,6224,452]

print("\n")
print(b)
c=[]
m=0
while m<(len(b)):
    c.append(b[(len(b)-m-1)])
    m+=1
print(c)


#direct assignment method with while loop
i=0
j=len(b)
print(b)
while i<j:
    b[i],b[j-1]=b[j-1],b[i]
    i+=1
    j-=1
print("revesrese is",b)

