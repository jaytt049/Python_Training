# Keeps asking until user enters valid number

while True:
    try:
        i = float(input("Enter Number : "))
        print("Your Number : ", i)
        break
    except ValueError:
        print("Enter Numbers only.")