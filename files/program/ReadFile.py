# Write a Python program to read a file line by line and store the lines in a list.

with open("test.txt", 'r') as file1:
    read = file1.read()
    print(read)
    file1.close()