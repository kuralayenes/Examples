
num1 = int(input("Number: "))

square = num1 ** 0.5

print("The square root of %0.3f is %0.3f"%(num1,square))



import cmath

# num = 1 + 6j
# or
num = eval(input("Enter a Number: "))

num_sqrt = cmath.sqrt(num)
print("The square root of {0} is {1:0.3f}+{2:0.3f}j".format(num, num_sqrt.real,num_sqrt.imag))