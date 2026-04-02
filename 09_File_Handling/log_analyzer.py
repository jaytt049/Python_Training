error = 0
info = 0

with open("data.txt", "r") as file:
    for line in file:
        if "ERROR" in line:
            error += 1 
        elif "INFO" in line:
            info += 1

print(f"total errors in log : {error}")
