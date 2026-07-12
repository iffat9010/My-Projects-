# CALCULATOR

print("Enter Your Name : ")
name = input()
print("Welcome to my Calculator", name)

print("Let's calculate your Number...")
print("And Rate Us")

print("+ is addition")
print("- is subtraction")
print("* is Multiply")
print("/ is divide")
print("// it shows int value {without decimal}")
print("% " "it shows remainder")

while True:
    a = int(input("Enter First Number : "))
    b = int(input("Enter Second Number : "))
    c = input("Enter your Operation ")

    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        if c == "0":
            print("Can not Divisible by Zero")
        else:
            print(a / b)
    elif c == "//":
        print(a // b)
    elif c == "%":
        print(a % b)
    else:
        print("Invalid Choice!! Try again")
    
# Break this calculator

    choice = input("Continue? (y/n): ")

    if choice == "n":
        break
