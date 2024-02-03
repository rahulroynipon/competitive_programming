n = int(input())
arr = list(map(int,input().split()))

big  = 0
small = 0

for i in range(n):
    if arr[big]<arr[i]:
        big = i
    
    if arr[small]>arr[i]:
        small = i

arr[small],arr[big] = arr[big], arr[small]

print(*arr)