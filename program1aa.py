list1=list((20,35,40,45,55,60))
print(list1)
#printed even dicvisibles list and multiplied with 2 made into new list
list2 = [2 * list1[x] for x in range(len(list1)) if list1[x] % 2 == 0]
print(list2)
#list2=[2*list1[x] if list1[x]%2==0 for x in range(len(list1))] # this is the error first need to write for loop followed by if
#print(list2)
list3=[list1[x]*2 for x in range (len(list1))]
print(list3)
list4=[list1[x]*2 if list1[x]%2==0 else list1[x] for x in range (len(list1)) ]#which is divisibele that element only multiplied
print(list4)
list5=[list1[x]*2 if x%2 == 0 else list1[x] for x in range(len(list1)) ]
print(list5)