l1=[2,34,23,423,43,4,2,9,1]
l2=[]
x=0
m=len(l1)
while(x<m):
    min_val=l1[0]
    for i in range (len(l1)-1):
        if min_val<l1[i+1]:
            min_val=min_val
        else:
            min_val=l1[i+1]
    print(min_val)
    l2.append(min_val)
    l1.remove(min_val)
    x+=1
print(l2)