def add(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    return a/b

print("please select one option to perform calculation task.")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
ch = int(input("Enter your Choice : "))
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))


if ch == 1:
    
    print(f"Addition : {add(num1, num2)}")
elif ch == 2:
    print(f"Substraction : {sub(num1, num2)}")
elif ch == 3:
    print(f"Multiplication : {mul(num1, num2)}")
elif ch == 4:
    print(f"Division : {div(num1, num2)}")
else:
    print("Invalid Input")