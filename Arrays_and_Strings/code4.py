# Given an integer array arr of size n, you need to sum the elements of arr.

def add(array1,n):
    sum=0
    for i in range(n):
        sum=sum+array1[i]
    print(sum)


array1=[10,20,30,50]
n=len(array1)
add(array1,n)

