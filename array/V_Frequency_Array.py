n, m = map(int,input().split())
arr = list(map(int,input().split()))

dict = {}

for value in arr:
    if value in dict:
        dict[value]+=1
    else:
        dict[value] = 1
    

for i in dict:
    print(dict[i])