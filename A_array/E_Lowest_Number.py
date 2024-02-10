n = int(input())
arr = list(map(int,input().split()))

small = 0

for i in range(n):
    if arr[small]>arr[i]:
        small = i

print(arr[small],small+1)