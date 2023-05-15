# Write a Python program to count the number of lines, words, and characters in a file.
count_line = 0
count_words = 0
count_character = 0
with open("test.txt", "r") as file1:
    for i in file1:
        count_line += 1
        count_words += len(i)
        count_character += len(i.split())
print("Count of Words is: ", count_words)
print("Count of Characters: ",count_character)
print("Count of lines: ",count_line)