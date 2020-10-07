
# Solution 1

def splitArr(arr,n,k):
    for i in range (0,k):
        x = arr[0]

        for j in range(0,n-1):
            arr[j] = arr[j+1]

        arr[n-1] = x


arrays = [4,5,6,1,2,3]
n = len(arrays)
position = 3

splitArr(arrays, n , position)

print(arrays)



