#Program to check if a year is a leap year:

count = int(input("Enter value"))
if count % 4 == 0:
    if count % 100 == 0:
        if count % 400 == 0:
            print(count, " is Leap Year")
        else:
            print(count, " is Not Leap Year")
    else:
        print(count, " is Leap Year")
else:
    print(count, " is Not Leap Year")
