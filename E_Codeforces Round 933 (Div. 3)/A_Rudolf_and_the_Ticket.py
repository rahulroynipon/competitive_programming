def decoder(a,b,total,arr1,arr2):
    count  = 0

    for i in arr1:
        if (i<total):
            for j in arr2:
                if (i+j<=total):
                    count+=1
    
    return count


if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        a, b, total = map(int, input().split())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        print(decoder(a, b, total, arr1, arr2))
