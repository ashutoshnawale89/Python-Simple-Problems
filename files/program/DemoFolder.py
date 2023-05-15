import os
import shutil

print(os.getcwd())
print(os.listdir())

# change directory
os.chdir('C:\\Users\\ASHUTOSH NAWALE\\Desktop')

print(os.getcwd())

# list all sub-directories
print(os.listdir())

print(os.listdir('C:\\ASHUTOSH\\E LEARNING COURSE VIDEO'))


#MAking new directories/folder
os.mkdir('Hello')
os.mkdir('new_one')

#Use of with...open Syntax
with open("C:\\Users\\ASHUTOSH NAWALE\\Desktop\\new_one\\test2.txt", "w") as file2:
    file2.write('This is python langauge  please understand carefully. ')
    file2.write("It is very sensitive langauge")

# rename a directory
os.rename('Hello','welcome')


# delete "myfile.txt" file
os.rmdir("welcome")

# delete "mydir" directory and all of its contents
shutil.rmtree("new_one")
