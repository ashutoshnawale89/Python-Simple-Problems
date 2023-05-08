#Program to check if a number is a perfect square:
from math import sqrt

count=int(input("Enter the Number"))
if count > 0:
    num=int(sqrt(count))
    if num*num == count :
        print("Perfect Square")
    else:
        print("Not Perfect Square")
else:
    print("Not Perfect Square")