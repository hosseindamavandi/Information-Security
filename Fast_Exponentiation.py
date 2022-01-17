#Fast Exponentiation

def exp(a,e,N):
    accum = 1
    i =0
    j =0
    
    while e:
        f=1
        i+=1
        while not (e%2):
            e /= 2
            a = ((a%N) * (a%N)) % N
            print("a: " , a)
            f=0
        if(f):
            print("a: " , a)
        
            
        e -= 1
        print("e: " , e)
        accum = ((accum%N) * (a%N)) % N
        print("accum: " , accum)
        print("____________________________")
    return accum


#######################
a = int(input("enter a (base): "))
e = int(input("enter e (power): "))
N = int(input("enter N (mod): "))

print(exp(a,e,N))
