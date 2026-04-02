#Handles: File not found

try:
    with open("file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File Not Found.")
except Exception as e:
    print("Error : ", e)
