n = int(input())
arr = list(map(int,input().split()))

new = arr.copy()

for i in range(n//2):
    new[i], new[n-1-i] = new[n-1-i], new[i]


print('YES' if arr==new else 'NO')