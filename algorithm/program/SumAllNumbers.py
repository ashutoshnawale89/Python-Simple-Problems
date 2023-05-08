#Write a Python function to calculate the sum of digits of a given number using recursion.


total_Value = 0
def sumValue(value):
    global total_Value
    if value == 0:
        return
    else:
        total_Value = value + total_Value
        sumValue(value - 1)

value = int(input("Enter the value : "))
sumValue(value)
print(total_Value)