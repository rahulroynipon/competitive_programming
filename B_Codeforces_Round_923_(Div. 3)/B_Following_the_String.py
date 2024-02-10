
def decoder(arr,n):
    myDict = {}
    new = [None]*n

    x = 97
    for j,i in enumerate(arr):
        if i==0:
            new[j] = chr(x)
            myDict[chr(x)] = 0
            x+=1
        else:
            search = i-1
            for key,value in myDict.items():
                if value==search:
                    new[j] = key
                    myDict[key]+=1
                    break
    ans = ''
    for i in new:
        ans+=i
    
    return ans

    


if __name__ == '__main__':
    
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        print(decoder(arr,n))


