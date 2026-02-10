#using flag method necessary
lis1=[1,2,3,4,5,6]
y=5
y=int(y)
for x in range(len(lis1)):
    if y == lis1[x]:
        print("element exist")
    else:
        print("doesnt exist")

#if element doesnt exist it repeating multiple times
print("\n")
lis1=[1,2,3,4,6,5]
y=5
y=int(y)
for x in range(len(lis1)):
    if y == lis1[x]:
        flag=True
        break
    else:
        flag=False
if flag:
    print("element  exist")
else:
    print("element doesnt exist")