number = int(input("Enter a number: "))

fact = 1
if number < 0 :
    print("Sorry Factorial does not exist for negative number.")
elif number == 0:
    print("The factorial of  0 is 1 ")
else:
    for i in range(2,number+1):

        fact = fact * i

    print("The factorial number is : ",fact)