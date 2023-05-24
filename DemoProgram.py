#Write a Python program to find the longest increasing subsequence in a given list of integers.

#This program finds and prints the longest increasing subsequence in the given list of integers.
# In the example usage, the input list is [10, 22, 9, 33, 21, 50, 41, 60], and the output would be
# [10, 22, 33, 50, 60], as it is the longest subsequence of increasing numbers within the list.


list_value = [10, 5, 19, 13, 2, 15, 41, 60]
result_value = []
length = range(len(list_value))

for i in length:
    for j in length:
        if len(list_value)-1 == j:
            break
        if list_value[j] > list_value[j+1]:
            result_value.append(list_value[j +1])
    for k in result_value:
        if k in list_value:
            list_value.remove(k)


print(list_value)