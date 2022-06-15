# Given an array of integers, find two numbers such that they add up to a specific target number.

def target(array1,sum):
    for i in range(0, len(array1)):
        for j in range(1,len(array1)):
            if array1[i]+array1[j]==sum:
                print(array1[i],",",array1[j])


array1 = [0, -1, 2, -3, 1]
target(array1,sum)
