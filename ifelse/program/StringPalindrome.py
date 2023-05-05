# Program to check if a string is a palindrome:

value = input("Enter value")
result = value[::-1]
if (value.lower()==result.lower()):
    print("Palindrome Value")
else:
    print("Not Palindrome Value")
