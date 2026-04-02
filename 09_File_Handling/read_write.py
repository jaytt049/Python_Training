with open("data.txt", "w") as file:
    file.write("INFO: Started")
    file.write("\nERROR: Something failed")
    file.write("\nINFO: Running")
    
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

with open("data.txt", "a") as file:
    file.write("\nERROR: Crash detected")

