# Write a Python program that uses try-except blocks to handle the
# "TypeError" exception when attempting to concatenate a string and a number.


try:
    num1 = 10.122
    value = "Hello"
    value2 = "Welcome"
    print(value + num1 + value2)
except TypeError:
    print("Type Error Please check the value ")