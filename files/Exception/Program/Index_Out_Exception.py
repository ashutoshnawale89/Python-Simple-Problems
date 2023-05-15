# Write a Python program that uses try-except blocks to handle the "Index out of range"
# exception when attempting to access an index that is outside the bounds of a list.

try:
    index = range(3)
    arr_list = [1, 2]
    for i in index:
        print(arr_list[i])
except ZeroDivisionError:
    print("Enter value is Zero ")
except IndexError:
    print("Index out of bond")
