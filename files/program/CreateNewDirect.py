import os
#Write a Python program to create a new directory and write a file into it.

#create new directories
os.mkdir('Test')
os.chdir('C:\\Users\\ASHUTOSH NAWALE\\PycharmProjects\\pythonProject\\files\\program\\Test')
print(os.getcwd())
with open("C:\\Users\\ASHUTOSH NAWALE\\PycharmProjects\\pythonProject\\files\\program\\Test\\file1.txt","w")as file1:
    file1.write("Welcome python program")
