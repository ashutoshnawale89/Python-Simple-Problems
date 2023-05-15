#Write a Python program that uses the "try-except-else" blocks to perform
# some operation and raise an exception if the operation fails.

def try_function():
    try:
        value = int(input("Enter value: "))
        num = 10/value
    except:
        print("Not divisible Number")
    else:
        print(value,"It is divisible number")

try_function()