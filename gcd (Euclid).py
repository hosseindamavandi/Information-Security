a=int(input("enter a: "))
b=int(input("enter b: "))

A=a
B=b

while B:
    print("B: " , B)
    R=A % B
    print("A % B: " , R)
    A=B
    B=R
    print("_____________________________________")

print(A)
