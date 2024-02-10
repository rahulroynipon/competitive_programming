t = int(input())

for _ in range(t):
    n  = int(input())
    arr = list(map(int,input().split()))

    ans = []
    for i in range(n):
        for j in range(i+1,n+1):
            new = arr[i:j]
            big = max(new)
            ans.append(big)
    
    print(*ans)