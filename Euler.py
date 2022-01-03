# Euler

import math

def phee(upper):
    cnt = 0
    lower = 1
    
    for num in range(lower,upper + 1):  
       if num > 1:  
           for i in range(2,num):  
               if (num % i) == 0:  
                   break  
           else:
               cnt+=1
               
    return cnt

########################

a = int(input("enter a: "))
N = int(input("enter N: "))

if math.gcd(a,N)==1 :
    Euler = pow(a,phee(N)) % N == 1
else:
    print("NOT")

print(Euler)
