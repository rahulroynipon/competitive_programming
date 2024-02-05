x, y = map(int, input().split())
arr = list(map(int, input().split()))

new = []

total = 0
for i in arr:
    total+=i
    new.append(total)



for _ in range(y):
    a,b = map(int, input().split())
    if a==1:
        print(new[b-1])
    else:
        ans = new[b-1]-new[a-2]
        print(ans)





