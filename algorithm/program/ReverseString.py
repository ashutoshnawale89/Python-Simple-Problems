#Write a Python function to reverse a string using recursion.

def reverse(value):
    if len(value) == 0:
        return value
    else:
        return reverse(value[1:]) + value[0]


value = "Life is Beautiful Enjoy Every Movement"

print("The original string is : ", value)

print("The reversed string(using recursion) is : ", reverse(value))
