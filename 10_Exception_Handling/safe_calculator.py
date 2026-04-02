try:
    a = float(input("Enter Number : "))
    b = float(input("Enter Number : "))
    op = input("Enter Operator (+,-,*,/) : ")

    if op == "+":
        print("Result : ", (a + b))
    elif op == "-":
        print("Result : ", (a - b))
    elif op == "*":
        print("Result : ", (a * b))
    elif op == "/":
        print("Result : ", (a / b))
    else:
        print("Invalid Operator")
except ValueError:
    print("Invalid Input! Enter Number Only.")
except ZeroDivisionError:
    print("Cannot devide by zero.")
except Exception as e:
    print("Something went wrong : ", e)