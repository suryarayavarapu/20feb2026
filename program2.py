x=int(input("how many number required in a list"))
y=0
numbers=[]
numbers_string=input("enter values by space")
list1=numbers_string.split(" ")
print(list1)
length=len(list1)
print(length)
while y<length:
    numbers.append(int(list1[y]))
    y+=1
print(numbers)   
#numbers.append()