def mul_gen(num):
    for i in range(1, 11):
        print(f"{num} X {i} = {num*i}")

n = int(input("Enter Number : "))
mul_gen(n)