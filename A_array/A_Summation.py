n = int(input())
arr = list(map(int,input().split()))

total = 0

for i in arr:
    total+=i

print(abs(total))