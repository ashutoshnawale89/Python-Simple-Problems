#Find the sum of all even numbers in a list

def sumEven(value):
    sum = 0
    for i in value:
        if i % 2 == 0:
            sum = sum + i
    print("Sum of Even Number is : ", sum)

value = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
sumEven(value)