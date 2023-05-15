# Write a Python program that uses try-except blocks to handle multiple exceptions,
# including "File not found", "Division by zero", and "Index out of range".

try:
    num = int(input("Enter value : "))
    value = 10/num
    print(value)

    index = range(3)
    arr_list = [1, 2]
    for i in index:
        print(arr_list[i])

    with open("test.txt") as file1:
     value = file1.read()
     print(value)
except ZeroDivisionError:
    print("Enter value is Zero ")
except IndexError:
    print("Index out of Range")
except FileNotFoundError:
    print("File does not exist ")
