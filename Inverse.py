import math


def inverse(m, b):
    A1 = 1
    A2 = 0
    A3 = m
    B1 = 0
    B2 = 1
    B3 = b
    while True:

        if B3 == 0:
            A3 = math.gcd(m, b)  # no inverse
            print("no inverse")
            return A3
        elif B3 == 1:
            B3 = math.gcd(m, b)  # B2=b^-1 mod m
            print("Inverse: " , B2)
            return B3
        Q = A3 // B3
        print("Q: " , Q )
        T1 = A1-Q*B1
        T2 = A2-Q*B2
        T3 = A3-Q*B3
        A1 = B1
        print("A1 " , A1 )
        A2 = B2
        print("A2 " ,A2 )
        A3 = B3
        print("A3 " , A3)
        B1 = T1
        print("B1 " ,B1 )
        B2 = T2
        print("B2 " ,B2 )
        B3 = T3
        print("B3 " , B3)
        print("_____________________________________________________")


#####################
b = int(input("enter number: "))
m = int(input("enter m(modul): "))


inverse(m, b)
