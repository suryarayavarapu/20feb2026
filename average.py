l1=[2,1,3,34,55,346,634,22,23,54,234,3465]
max=2
for i in range(len(l1)-1):
    if max>l1[i+1]:
        max=max
    else:
        max=l1[i+1]
print(max)
l2=[3423,25346,245,2656,562]
res=max(l2)
print(res)