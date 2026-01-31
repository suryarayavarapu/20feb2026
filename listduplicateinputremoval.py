list4=[]
i=0
n=int(input("enter list length"))
while i<n:
    x=int(input("enter values one by one"))
    if x in list4:
        print("you are enterinfg duplicate values")
    else :
        list4.append(x)
    i+=1
print(list4)