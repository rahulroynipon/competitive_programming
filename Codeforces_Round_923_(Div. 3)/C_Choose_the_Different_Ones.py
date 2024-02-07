def decoder(a,b,k,arrA,arrB):
    half = k//2
    arrA = set(filter(lambda x: x <= k, arrA))
    arrB = set(filter(lambda x: x <= k, arrB))

    if len(arrA)<half or len(arrB)<half:
        return 'NO'

    countA = 0
    countB = 0
    both = 0

    for i in range(1,k+1):
        if (i in arrA) and (i in arrB):
            both+=1
        elif i in arrA:
            countA+=1
        elif i in arrB:
            countB+=1
    
    if (countA+countB+both)==k:
        return 'YES'
    
    return 'NO'
    

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        a,b,k = map(int,input().split())
        arrA = list(map(int,input().split()))
        arrB = list(map(int,input().split()))
        print(decoder(a,b,k,arrA,arrB))