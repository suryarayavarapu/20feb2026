l1=[4,2,7,3]
l2=[1,2,3,1]
if l1==l2:
    print("equal")
else:
    print("not equal")

print("\n")
if (len(l1))==(len(l2)):
    for i in l1:
        if i in l2:
            print(i," is there")
        else :
            print(i, "not there")
else:
    print("length not equal so not identical")