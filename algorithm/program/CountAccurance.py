# Write a Python program to count the number of occurrences of a given element in a list using recursion.

count = 0
def countAccurance(arr_list , key):
    global  count
    for i in arr_list:
        if i == key:
            count = count + 1
    if count != 0:
        print(" The value of ", key, " is ", count, "times")
    else:
        print(key ,"Key Not found....Please check the list")

arr_list = [45,78,45,89,7,52,85,63,48,45]
countAccurance(arr_list, 5)
