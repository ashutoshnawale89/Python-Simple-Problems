#Program to check if a triangle is equilateral, isosceles, or scalene:

value1=int(input("Enter Triangle one side lenth "))
value2=int(input("Enter Triangle second side lenth"))
value3=int(input("Enter Triangle third side lenth"))

if (value1==value2 and value2==value3):
    print("The Given Triangle is equilateral")
elif (value1==value2 or value2==value3 or value1==value3):
    print("The given Triangle is isosceles")
else:
    print("The given Triangle is scalene")
