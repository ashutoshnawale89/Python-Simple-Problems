#Write a program that takes a list of strings as input and
# outputs a new list containing only the strings that have more than 5 characters.

loop_length= range(int(input("Enter loop length : ")))
value_list = [""]

for i in loop_length:
    input_value = input("Enter The Value : ")
    value_list.insert(i,input_value)

new_value_list = [""]
index = 1
for num in value_list:
    count=0
    for i in num:
        count = count + 1
    if count > 5:
        new_value_list.insert(index , num)
        print(num)
        index = index + 1



