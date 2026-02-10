l1=[1,2,34,5,2,4435]
l2=[2,5,1]
for v1 in l2:
    while v1 in l1:
        l1.remove(v1)
print(l1)