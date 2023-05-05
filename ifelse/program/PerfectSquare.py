#Program to check if a number is a perfect square:
from math import sqrt

value=int(input("Enter the Number"))
if value > 0:
    num=int(sqrt(value))
    if num*num == value :
        print("Perfect Square")
    else:
        print("Not Perfect Square")
else:
    print("Not Perfect Square")