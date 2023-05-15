# Write a Python program that uses try-except blocks to handle the "Division by zero" exception
# when attempting to divide a number by zero.

try:
    num = int(input("Enter value : "))
    value = 10/num
    print(value)
except ZeroDivisionError:
    print("Enter value is Zero ")