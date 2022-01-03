# Fermat's

import math

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

##################

a=int(input("enter a: "))
p=int(input("enter p: "))

if math.gcd(a , p)==1 and isPrime(p)==True :
    fermat = pow(a,p-1) % p
    print(fermat)

else:
    print("not Prime a,p")

