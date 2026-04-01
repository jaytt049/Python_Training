#simple interest = principle*rate*time/100

Principle = float(input("Enter Principle : "))
Rate = float(input("Enter Rate of Interest (R%) : "))
Time = float(input("Enter Time (years) : "))

simple_interest = (Principle*Rate*Time)/100

amount = Principle + simple_interest

print(f"Simple Interest : {simple_interest}")
print(f"total amount : {amount} ")