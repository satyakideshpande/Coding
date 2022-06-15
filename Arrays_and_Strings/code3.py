# Perform search, insert and delete on an array
def search(a, num):
    for i in range(len(a)):
        #print(i)
        # print(a[i])
        if a[i] == num:
            print(a[i])



a = [10, 20, 30, 40]
num = 30
search(a, num)
