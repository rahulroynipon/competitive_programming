def arranger(n,cat,seat):
    cat = list(map(int,cat))
    seat = list(map(int,seat))

    Ncat = sum(cat)
    Nseat = sum(seat)

    operation = 0
    if Ncat>=Nseat:
        operation = Ncat - Nseat
    for i in range(n):
            if seat[i]==1:
                if seat[i]!=cat[i]:
                    operation+=1
    
           
    return operation




if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        cat = input()
        seat = input()
        print(arranger(n,cat,seat))