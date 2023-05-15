# Write a Python program to find the longest word in a file.

count_word = ""
largest_word = ""
with open("test.txt","r") as file1:
    for i in file1:
        count_word = i.split()
        for j in count_word:
            if largest_word < j:
                largest_word = j

print("Largest Word is : ", largest_word)


