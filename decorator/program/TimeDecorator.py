# Implement a decorator @timer that measures the execution time of a function and prints it.
from time import time

def timeDecoratorFunction(func):
    def subTimeDecoratorFunction(value):
        start_Time = time()
        func(value)
        end_Time = time()
        return end_Time-start_Time,"sec"
    return subTimeDecoratorFunction
@timeDecoratorFunction
def ordinaryTime(value):
    for i in range(value):
        sum = i
    return

value =int(input("Enter the loop Iteration number : "))
print(ordinaryTime(value))
