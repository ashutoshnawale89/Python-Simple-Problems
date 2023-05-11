#Longest Word: Find the longest word in a sentence

def findlong_Sentence():
    long_sentence = input("Enter the long sentence ")
    list_value = long_sentence.split(" ")
    print(list_value)

    temp_value = ""
    for i in list_value:
        if i > temp_value:
            temp_value = i
    print("The Greatest value is : ", temp_value)
findlong_Sentence()