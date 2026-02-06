def func1(arr):
   for i in range (len(list1)):
    arr.append(int(list1[i]))
    print(arr[i],end =" \n")
list1=input("enter values by space it will take into string")
print(list1)
print(type(list1))
list1=list1.split(" ")
arr=[]
func1(arr)
print(len(arr))
sum =0
for x in range(len(arr)):
  sum =sum+arr[x]
print(sum)
for z in range(len(arr)):
  arr[z]=arr[z]-1
print(arr)