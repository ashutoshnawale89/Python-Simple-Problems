#Write a Python program to check whether a file exists or not.

try:
    with open("test.txt") as file1:
        print("file does exist")
except:
    print("file does not exist")