#Fast Exponentiation

def exp(a,e,N):
    accum = 1
    while e:
        while not (e%2):
            e /= 2
            a = ((a%N) * (a%N)) % N
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
