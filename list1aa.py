#enumerate usage
list1=list((2,3,4,56))
for index,value in enumerate(list1):# in bracked dont miss list1 variable
    if index%2!=0:
        list1[index]=list1[index]*2
print(list1)

#lambda and map, increment index values to 1
list2=[10,5,5,2,4,3,4]
list2=list(map(lambda x:x+1, list2))
print(list2)


x=6
x= int (x)
for y in range(len(list2)):
    if x == list2[y]:
        print(y)


print("\n")
x=5
x= int (x)
new_list=[]
for y in range(len(list2)):
    if x == list2[y]:
        new_list.append(list2[y])
        print(y)
print(new_list)