t = int(input())
 
for _ in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    d = list(map(int, input().split()))
 
    y = [b, c, d]
    x = a[0]
 
    for i in y:
        if x == i[0]:
            length = abs(a[1] - i[1])
            break
 
    print(length ** 2)