num = int(input("Enter a Number: "))

# (n*(n+1))/2

if num < 0:
    print("Enter a possitive number.")
else:

    sum = 0

    for i in range(num+1):
        sum = sum + i

    print("The sum is ",sum)