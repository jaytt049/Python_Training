with open("contacts.txt", "a") as file:
    name = input("Enter name: ")
    number = input("Enter number: ")

    file.write(name + "," + number + "\n")

with open("contacts.txt", "r") as file:
    for line in file:
        name, number = line.strip().split(",")
        print("Name:", name, "| Number:", number)