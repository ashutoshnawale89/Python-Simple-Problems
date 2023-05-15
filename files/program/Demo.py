# open file in current directory
import os

file1 = open("test.txt", 'r')
read = file1.read()
print(read)
file1.close()

#Use of with...open Syntax
with open("test2.txt", "w") as file2:
    file2.write('This is python langauge  please understand carefully. ')
    file2.write("It is very sensitive langauge")

file1 = open("test.txt", 'a')
file1.write('This is python langauge  please understand carefully. ')
file1.write("It is very sensitive langauge")
file1.close()

#delete the txt file
os.remove("test.txt")
os.remove("test2.txt")

with open("test.txt", "w") as file2:
    file2.write('This is python langauge  please understand carefully. ')
    file2.write("It is very sensitive langauge")
