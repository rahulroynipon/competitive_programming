t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))

    ans = []

    for i in range(n):
        for j in range(i+1,n):
            x = arr[i] + arr[j] + j - i
            ans.append(x)
    
    print(min(ans))
