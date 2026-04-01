a = float(input("Enter Number 1 (a) : "))
b = float(input("Enter Number 2 (b) : "))
c = float(input("Enter Number 3 (c) : "))

if a == b == c:
    print("All numbers are equal")
elif a == b or a == c:
    print("Two numbers are equal and greatest:", a)
elif b == c:
    print("Two numbers are equal and greatest:", b)
elif a > b and a > c:
    print("a is greatest")
elif b > a and b > c:
    print("b is greatest")
else:
    print("c is greatest")
