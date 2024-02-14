def start(arr,n):
    count = 0
    sArr = arr[0]
    for i in range(n):
        if arr[i]==sArr:
            count+=1
        else:
            return count

def end(arr,n):
    count = 0
    eArr = arr[n-1]
    for i in range(n-1,-1,-1):
        if arr[i]==eArr:
            count+=1
        else:
            return count

def decoder(arr,n):
    if len(set(arr))==1:
        return 0

    s = start(arr,n)
    e = end(arr,n)
    
    
    
    if arr[0]==arr[-1]:
        return n-s-e
    
    if s>e:
        return n-s
    else:
        return n-e
    




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print(decoder(arr,n))