def decoder(n,arr):
    if n==1:
        return 'YES'
    
    total = sum(arr)
    half = total//n

    if arr[0]<half:
        return 'NO'
    
    save = 0
    for i in range(n):
        if arr[i]>half:
            save = save + (arr[i]-half)
            arr[i] = half
            
        
        elif arr[i]<half:
            save = save + (arr[i]-half)
            arr[i] = half
        
        if save<0:
            return 'NO'
    
    return 'YES'


        
        
    


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print(decoder(n,arr))

