A = [[12,7],
     [4,5],
     [3,8]]

result = [[0,0,0],
          [0,0,0]]

for i in range(len(A)):

    for j in range(len(A[0])):

        result[j][i] = A[i][j]

for z in result:
    print(z)