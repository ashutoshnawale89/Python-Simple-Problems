# open a file
import os
import shutil

print("Previous directory", os.getcwd())
# change directory
# os.chdir('C:\\GE')
# print("After Change directory", os.getcwd())
# print(os.listdir())
# print(os.listdir('D:\\'))
# os.mkdir('Test')
# os.rename('Test', 'new_one')
# print(os.chdir('C:\\Users\\user\\PycharmProjects\\pythonProject\\Test'))
# open("text.txt", 'w')
# os.remove("text.txt")
# os.rmdir("Test")
shutil.rmtree("Test")

# try:
#     # file1 = open("test3.txt")
#     # file1.close()
#     with open("test3.txt", 'w') as file1:
#         file1.write('Programming is Fun.\n')
#         file1.write('Programiz for beginners')
#
#     with open("test3.txt") as file2:
#         print(file2.read())
#
#     os.remove("myfile.txt")
#
# except:
#     print("File not found")
#     # file1.close()