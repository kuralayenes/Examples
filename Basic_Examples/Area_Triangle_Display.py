

num1 = float(input("Enter number1 : "))
num2 = float(input("Enter number2 : "))
num3 = float(input("Enter number3 : "))


s = (num1+num2+num3)/2
area = (s*(s-num1)*(s-num2)*(s-num3))**0.5

print("The area of the triangle is %0.2f" %area)