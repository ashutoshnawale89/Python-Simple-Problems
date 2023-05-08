#Write a program that takes a list of numbers as input and
# outputs a new list containing only the odd numbers in the original list.

loop_length1 = range(int(input("Enter loop length 1 : ")))
value_list1 = []
result_list = []
index = 0
for i in loop_length1:
    count = int(input("Enter list-1 Value : "))
    value_list1.insert(i, count)
    if count % 2 != 0:
        result_list.insert(index, count)
        index += index
print(" Odd Number is : ", result_list)
