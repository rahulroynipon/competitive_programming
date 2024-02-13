def decoder(n):
    
    if n%2==0 and n<=26:
        x = 'a'
        y = chr(96+n-2)

        return x+x+y
    
    elif n%2==1 and n<=26:
        return 'aa'+chr(96+n-2)
        
    else:
        count = 0
        y = n
        while y>26:
            count+=1
            y-=26
            
        if count==1:
            if y>1:
                return 'a'+chr(95+(n-26))+chr(96+26)
            else:
                return 'aa'+chr(96+n-y-1)
        elif count==2:
            return chr(96+y)+'zz'
        else:
            return 'zzz'
            
            

    


if __name__ == '__main__':
    t =int(input())
    for i in range(t):
        n = int(input())
        print(decoder(n))
    

