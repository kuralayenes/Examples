
A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[19,13,11],
     [61,52,43],
     [13,21,12]]

result= [[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range(len(A)):
    for j in range(len(B)):
        result[i][j] = A[i][j] + B[i][j]

for z in result:
    print(z)