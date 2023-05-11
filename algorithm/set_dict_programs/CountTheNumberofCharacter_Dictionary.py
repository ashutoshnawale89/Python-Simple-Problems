#Dictionary program: Count the number of occurrences of each character in a string using a dictionary

def counCharacterInString():
    str_value = input("Enter the value of Count Character : ")
    count_Character = {}
    list_value = []
    for i in str_value:
        count = 0
        if i not in list_value:
            list_value.append(i)
            for j in str_value:
                if i == j:
                    count = count + 1
            count_Character[i] = count
            print(i , count)

    print(count_Character)


counCharacterInString()