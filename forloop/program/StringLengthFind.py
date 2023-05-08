#Write a program that takes a list of strings as input and
# outputs a new list containing the length of each string in the original list.

loop_length1 = range(int(input("Enter loop length 1 : ")))
value_list1 = []
result_list = []

for i in loop_length1:
    count = input("Enter list-1 Value : ")
    value_list1.insert(i, count)
index = 0
for count in value_list1:
    count = 0
    for i in count:
        count = count + 1
    else:
        result_list.insert(index, count)
        index = index + 1

print(" Original List is : ", value_list1)
print(" New List is : ", result_list)