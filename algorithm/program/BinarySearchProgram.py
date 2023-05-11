#Write a Python program to implement the binary search algorithm using recursion.

count = 0
def search(value,key):
    global count
    if len(value) == count:
        print("Not Found in List")
        return 
    if value[count] == key:
        print("The value of ", key, " is ", count, " index")
    else:
        count = count + 1
        search(value, key)

value = [5,10,45,7,85,14,96,12,14,86,22]
key = int(input("Enter value : "))
search(value, key)