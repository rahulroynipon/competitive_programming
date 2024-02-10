def decoder(arr,count):
    for i in arr:
        if i%2==1:
            return count

    for i in range(len(arr)):
        arr[i] = arr[i]//2
    
    return decoder(arr,count+1)



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().split()))
    print(decoder(arr,0))