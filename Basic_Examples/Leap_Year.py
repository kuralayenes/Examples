year = int(input("Enter a Year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            if year % 4000 == 0:
                print("Not Leap Year")
            else:
                print("Leap Year")
        else:
            print("Not Leap Year")
    else:
        print("Leap Year")
else:
    print("Not Leap Year")
