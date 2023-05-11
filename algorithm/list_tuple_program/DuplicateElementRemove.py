#List program: Remove duplicates from a list

def duplicate():
    list_value = []
    index = range(int(input("Enter the size of list : ")))
    for i in index:
        value = input("Enter value : ")
        list_value.append(value)
    print(list_value)
    for i in list_value:
        count = -1
        for j in list_value:
            if i == j:
                count = count + 1
        if count == 1:
            list_value.remove(i)
    print(list_value)

duplicate()