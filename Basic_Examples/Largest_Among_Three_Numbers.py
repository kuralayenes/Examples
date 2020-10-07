num1 = float(input("Enter a number1: "))
num2 = float(input("Enter a number2: "))
num3 = float(input("Enter a number3: "))

if num1>=num2 and num1>=num3:
    print("Number1 Largest")
elif num2>=num1 and num2>=num3:
    print("Number2 Largest")
else:
    print("Number3 Largest")