user = str(input("Enter Your Name : "))
print(f"Hello {user}!\n")
print("please select one option to perform calculation task.")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
ch = int(input("Enter your Choice : "))
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))


if ch == 1:
    add = num1+num2
    print(f"Addition : {add}")
elif ch == 2:
    sub = num1-num2
    print(f"Substraction : {sub}")
elif ch == 3:
    mul = num1*num2
    print(f"Multiplication : {mul}")
elif ch == 4:
    div = num1/num2
    print(f"Division : {div}")
else:
    print("Invalid Input")