n = int(input())
arr = list(map(int,input().split()))

for i in range(n):
    if arr[i]>0:
        arr[i] = 1
    elif arr[i]<0:
        arr[i] = 2

print(*arr)