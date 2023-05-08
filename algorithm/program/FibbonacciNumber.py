#Python program that uses functions and recursion to
# calculate the nth Fibonacci number:

count = 2
fibbo_Value1 = 0
fibbo_Value2 = 1
sum_Fibbo = 1

def fibbonacci(number):
    global count, fibbo_Value2, fibbo_Value1, sum_Fibbo
    if count == 2:
        count = number
        number = 1
        print(fibbo_Value1)
        print(fibbo_Value2)
        print(sum_Fibbo)

    if number != count:
        fibbo_Value1 = fibbo_Value2
        fibbo_Value2 = sum_Fibbo
        sum_Fibbo = fibbo_Value2 + fibbo_Value1
        print(sum_Fibbo)
        number = number + 1
        fibbonacci(number)

value = int(input("Enter the value of Fibbonacci Range :  "))
fibbonacci(value)

