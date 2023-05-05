#Write a program that takes a list of numbers as input and
# outputs a new list containing the square of each number in the original list.

loop_length1 = range(int(input("Enter loop length 1 : ")))
value_list1 = []
result_list = []

for i in loop_length1:
    value = int(input("Enter list-1 Value : "))
    new_value = value * value
    value_list1.insert(i, value)
    result_list.insert(i, new_value)

print(" Original List is : ", value_list1)
print(" New List is : ", result_list)
