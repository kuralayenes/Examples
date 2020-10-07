def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n-1)
num = 6

if num < 0:
    print("Please Enter a Positive Number.")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of ",num,"is",fact(num))