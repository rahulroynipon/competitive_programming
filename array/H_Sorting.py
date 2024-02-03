n = int(input())
arr = list(map(int,input().split()))

for _ in range(n):
    for i in range(n-1):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

print(*arr)