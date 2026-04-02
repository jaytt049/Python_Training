a = float(input("Enter Number 1 (a): "))
b = float(input("Enter Number 2 (b): "))
c = float(input("Enter Number 3 (c): "))

if a == b == c:
    print("All numbers are equal")

elif a >= b and a >= c:
    if a == b or a == c:
        print("Two numbers are equal and greatest:", a)
    else:
        print("a is greatest")

elif b >= a and b >= c:
    if b == c:
        print("Two numbers are equal and greatest:", b)
    else:
        print("b is greatest")

else:
    print("c is greatest")