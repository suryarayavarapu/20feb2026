nums=[4,2,3,3,4,4,5,1,7,9,9,6,4]
x=0
printed=set()
y=0
for x in range (len(nums)):
    count=0
    for y in range(len(nums)):  
        if nums[x]==nums[y]:
            count+=1
            if count > 1 and nums[x] not in printed:
                print("duplicate is", nums[x],"and repeated this number is more than",count,"times.")
                printed.add(nums[x])
print(nums)
#for no duplicates and ascending order
new=set(nums)
print(new)