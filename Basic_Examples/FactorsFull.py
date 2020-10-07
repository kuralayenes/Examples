num = int(input("Enter a Number: "))

def print_facts(x):

    for i in range(1,x+1):

        if x % i == 0:
            print(i)

print_facts(num)