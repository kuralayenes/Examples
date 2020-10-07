num = int(input("Enter a number: "))

sum = 0

numd = num

while numd > 0:
    digit  = numd % 10
    sum += digit**3
    numd //= 10


if num == sum:
    print(num,"is a Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")