# Program to check if a string is a palindrome:

count = input("Enter value")
result = count[::-1]
if (count.lower()==result.lower()):
    print("Palindrome Value")
else:
    print("Not Palindrome Value")
