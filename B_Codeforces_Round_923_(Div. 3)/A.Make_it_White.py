def decoder(n,arr):

    s = None
    e = None
    for i in range(n):
        if (s==None and arr[i]=='B'):
            s = i
        if (e==None and arr[n-1-i]=='B'):
            e = n-i
        
        if (e!=None and s!=None):
            break
    
    ans = e-s

    return ans


if __name__ == '__main__':
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input()
        print(decoder(n,arr))

