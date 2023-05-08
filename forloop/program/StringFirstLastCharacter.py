#Write a program that takes a string as input and
# outputs a new string containing only the first and last characters of the original string.

count = input("Enter value as String : ")
result = ""
count1 = 0
count2 = len(count) - 1
index = 0
for i in count:
    if(count1 == index or count2 == index):
        result = result + i
    index = index + 1
print(result)