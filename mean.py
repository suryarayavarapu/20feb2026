import statistics
l1=[1,2,3,4,5,6,7,8,9,10]
res=statistics.mean(l1)
print(res)

# intersection of 2 lists
l2=[4,6,43,2,2,24,4,6,1]
l3=list(set(l1) and set(l2))
print(l3)

