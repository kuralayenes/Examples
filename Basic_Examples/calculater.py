
def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y




while True:


    num1 = float(input("Enter a number1: "))
    num2 = float(input("Enter a number2: "))

    print("Choose Operation")
    print("1 - Add")
    print("2 - Subtract")
    print("3 - Multiply")
    print("4 - Divide")

    choice = input("Enter Operation(1/2/3/4): ")

    if choice in ("1","2","3","4"):

        if choice == "1":
            print(add(num1,num2))
        elif choice == "2":
            print(subtract(num1,num2))
        elif choice == "3":
            print(multiply(num1,num2))
        elif choice == "4":
            print(divide(num1,num2))

    else:
        print("Invalid Input Please Try Again !! ")