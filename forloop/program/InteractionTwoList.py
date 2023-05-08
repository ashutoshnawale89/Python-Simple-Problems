#Write a program that takes two lists of integers as input and
# outputs a new list containing the intersection of the two lists
# (i.e., the numbers that appear in both lists).

loop_length1 = range(int(input("Enter loop length 1 : ")))
loop_length2 = range(int(input("Enter loop length 2 : ")))

value_list1 = []
value_list2 = []
result_list = []
index = 0

for i in loop_length1:
    count = int(input("Enter list-1 Value : "))
    value_list1.insert(i, count)

for i in loop_length2:
    count = int(input("Enter list-2 Value : "))
    value_list2.insert(i, count)

for i in value_list1:
    for j in value_list2:
        count = 0
        if i == j:
            for k in result_list:
                if k == i:
                    count = count + 1
            if count == 0:
                result_list.insert(index, j)
                index = index + 1

for i in result_list:
    print(i)
