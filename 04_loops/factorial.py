def factorial(num):
    out = 1
    if num < 0:
        print("Factorial of Negative Not possible")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        for i in range(2, num+1):
            out = i*out
        print(f"Factorial of {num} is {out}")
Input = int(input("Enter Num : "))
factorial(Input)