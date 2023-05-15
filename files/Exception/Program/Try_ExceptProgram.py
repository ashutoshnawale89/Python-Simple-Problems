# Write a Python program that uses try-except blocks to handle the "File not found" exception when attempting to read a file

try:
    with open("test.txt") as file1:
     value = file1.read()
     print(value)
except FileNotFoundError:
    print("File not found")
