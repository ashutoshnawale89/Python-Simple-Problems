#Write a program that takes a list of strings as input and
# outputs a new list containing only the strings that start with a vowel (a, e, i, o, u).

list_index = range(int(input("Enter the size of list  :  ")))
count = []
result = []
for i in list_index:
    arr_value = input("Enter the words  : ").lower()
    count.insert(i, arr_value)

for i in count:
    count = 0
    for j in i:
        if count == 0:
            if j == "a" or j == "e" or j == "i" or j == "o" or j == "u":
                print(i)
                break
            count = 1

