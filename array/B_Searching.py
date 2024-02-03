n = int(input())
arr  = list(map(int,input().split()))
number = int(input())

found = -1

for i in range(n):
    if arr[i]==number:
        found = i
        break

print(found)