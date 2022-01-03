
def fact(n): 
    res = 1
    for i in range(2, n+1): 
        res = res * i 
    return res

def nCr(n, r): 
    return (fact(n) / (fact(r)* fact(n - r))) 
  
###########################
temp = 365
r = int(input("enter n: "))

NCR = int(nCr(temp, r))


out = (fact(r) * NCR) / pow(365,r)

output = "{:.3f}".format(out)

print("probability: " , output)
