import time
MAX = 1000000
def binarySearch(A, x, low, high):
    if (low > high):
        return -1
    else:
        mid = int((low+high) / 2)
        if (x == A[mid]):
            return mid
        elif x > A[mid]:
            return binarySearch(A,x,mid+1,high)
        else:
            return binarySearch(A,x,low,mid-1)

def linearSearch(A, n, x):
    i = 0
    while (i < n):
        if (A[i] == x):
            return i
        i+=1
    return -1

A = []
i = 0


j = 1
while j <= 20:
    while len(A) < MAX*j*10:
        A.append(i)
        i+=1
    start = time.time()
    linearSearch(A,len(A),-1)
    end = time.time()
    #print(MAX*j*10)
    print(" ")
    print("Linear Search :",(end-start) * 10**3, "ms")
    
    start2 = time.time()
    binarySearch(A,-1,0,len(A))
    end2 = time.time()
    print("Binary Search :",(end2-start2) * 10**3, "ms")
    j += 1
