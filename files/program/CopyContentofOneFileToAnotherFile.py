#Write a Python program to copy the contents of one file to another file.

with open("test.txt","r") as file1:
    value = file1.read()
    with open("test1.txt","w") as file2:
        file2.write(value)
