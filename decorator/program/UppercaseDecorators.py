# Write a decorator @uppercase that converts the return value of a function to uppercase.

def upperCase(func):
    def subCase(value):
        return func(value.upper())
    return subCase

@upperCase
def ordinaryFunction(value):
    print(value)

ordinaryFunction("hhhhhhh")
