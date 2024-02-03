n = int(input())
arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))


for i in range(n):
    for j in range(n-1):
        if arrA[j]>arrA[j+1]:
            arrA[j], arrA[j+1] = arrA[j+1], arrA[j]

        if arrB[j]>arrB[j+1]:
            arrB[j], arrB[j+1] = arrB[j+1], arrB[j]

print('yes' if arrA==arrB else 'no')