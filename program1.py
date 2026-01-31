nums=[4,2,3,3,4,4,5,1,7,9,9,6,4]
print(len(nums))
new=set(nums)
print (new)
list1=list(new)
x=0
printed=set()
y=0
for x in range (len(list1)):
    count=0
    for y in range(len(nums)):  
        if list1[x]==nums[y]:
            count+=1
    print( list1[x],count)
#task1 duplicate elements need to remove 
#each duplicate elements count i.e., element repeated n times
#in input dont take duplicate elements


