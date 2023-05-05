#Program to check if a year is a leap year:

value = int(input("Enter value"))
if value % 4 == 0:
    if value % 100 == 0:
        if value % 400 == 0:
            print(value, " is Leap Year")
        else:
            print(value, " is Not Leap Year")
    else:
        print(value, " is Leap Year")
else:
    print(value, " is Not Leap Year")
