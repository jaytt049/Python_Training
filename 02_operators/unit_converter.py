#miles = km*0.621371
#fahrenheit = (celsius * 9/5) + 32

print("1. KM to Miles")
print("2. Celsius to Fahrenheit")

choice = int(input("Enter your choice : "))

if choice == 1:
    km = float(input("Enter distance in KM: "))
    miles = km * 0.621371
    print("Distance in Miles =", miles)
elif choice == 2:
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit =", fahrenheit)
else:
    print("Invalid choice")