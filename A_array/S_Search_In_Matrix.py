n, m = map(int,input().split())
matrix = []
for i in range(n):
    arr = list(map(int,input().split()))
    matrix.append(arr)

x = int(input())

found = False

for i in range(n):
    for j in range(m):
        if matrix[i][j]==x:
            found = True
            break

print('will not take number' if found else 'will take number')

