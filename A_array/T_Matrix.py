n = int(input())

matrix = []

for _ in range(n):
    arr = list(map(int,input().split()))
    matrix.append(arr)

main = 0
second = 0

for i in range(n):
    for j in range(n):
        if i==j:
            main+=matrix[i][j]
        
        if j==n-1-i:
            second+=matrix[i][j]


print(abs(main-second))
