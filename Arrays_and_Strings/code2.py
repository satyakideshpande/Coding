# You are given an array A of size N.
# You need to print elements of A in alternate order (starting from index 0).
# eg A=[1,2,3,4] Output : 1 3


def alternate(A,n):
    for i in range(n):
        if i%2==0:
            print(A[i])


A=[1,2,3,4,5,6,7,8,9]
n=len(A)
alternate(A,n)