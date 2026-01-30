n=5
i=0
nums=[]
while(i<n):
    integer=int(input("enter value %d of list"%i))
    nums.append(integer)
    i+=1
print("i took numbers nums:",i,nums)
x=0
for x in range(n):
    if x<n:
        if x in nums:
            print("duplicate exist")