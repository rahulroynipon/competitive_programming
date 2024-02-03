n = int(input())

if n==1:
    print(0)
elif n==2:
    print(1)
else:
    frist = 0
    second = 1
    for _ in range(n-2):
        total = frist + second
        frist = second
        second = total
    
    print(total)
