#Write a program that takes a string as input and
# outputs the number of vowels (a, e, i, o, u) in the string.

value = input("Enter The value : ").lower()
print("Print the Vowels Character in String variables")
for i in value:
    if ("a"==i or "e"==i or "i"==i or "o"==i or "u"==i):
        print(i)