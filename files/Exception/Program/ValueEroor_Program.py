# Write a Python program that uses try-except blocks to handle
# the "ValueError" exception when attempting to convert a string to a float.

try:
    num = float(input("Enter value : "))
    value = 10/num
    print(value)
except ZeroDivisionError:
    print("Enter value is Zero ")
except ValueError:
    print("Can not be coverted String to float . To loss Data")