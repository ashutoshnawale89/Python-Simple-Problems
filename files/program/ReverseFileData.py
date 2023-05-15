# Write a Python program to read a file and print the contents in reverse order.

with open("test.txt", "r") as file1:
    for i in file1:
        value = " "
        for j in i:
            value = j + value
        print(value)