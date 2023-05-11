#Count Characters: Count the number of times a character appears in a string

def countCharacter():
    str_value = input("Enter the value : ")
    list_value = []
    for i in str_value:
        count = 0
        if i not in list_value:
            for j in str_value:
                list_value.append(i)
                if i == j:
                    count = count + 1
        if count != 0:
            print(i, "is the count is : ", count)

countCharacter()