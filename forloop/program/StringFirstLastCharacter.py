#Write a program that takes a string as input and
# outputs a new string containing only the first and last characters of the original string.

value = input("Enter value as String : ")
result = ""
count1 = 0
count2 = len(value)-1
index = 0
for i in value:
    if(count1 == index or count2 == index):
        result = result + i
    index = index + 1
print(result)