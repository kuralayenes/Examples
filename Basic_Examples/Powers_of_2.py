num = int(input("Enter a number: "))

for i in range(1, num+1):

    print("2 to raised the power",i,"is",2**i)


# Map Func


result = list(map(lambda x: 2 ** x,range(num)))


print("The total terms are:",num)

for i in range(num):
    print("2 to raised the power", i,"is",result[i])