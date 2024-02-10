n,m = map(int,input().split())

matrix = []
for _ in range(n):
    arr = list(map(int,input().split()))
    matrix.append(arr)


for i in range(n):
    for j in range(m//2):
        matrix[i][j],matrix[i][m-1-j] = matrix[i][m-1-j], matrix[i][j]
    
    print(*matrix[i])