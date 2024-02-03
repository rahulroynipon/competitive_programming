n = int(input())
arr = list(map(int,input().split()))

small = min(arr)

count = 0
for i in range(n):
    if arr[i] == small:
        count+=1

print('Lucky' if count%2==1 else 'Unlucky')