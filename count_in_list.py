a=[2,4,3,4,3,2,5,2,4,2,5,663,2]
print(a.count(5))
print(a.count(2))

#using for loop count
count=0
x=2
for i in range(len(a)):
    if x==a[i]:
        count+=1
print("\n",count)


#operator counter
import operator
print(operator.countOf(a,3))

#counter from collections
from collections import Counter
res=Counter(a)
print(res[4])