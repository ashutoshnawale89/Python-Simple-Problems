# String program: Count the number of vowels in a string

tuple_vowels = ("a", "e", "i", "o", "u")
def count(str_value):
    for i in str_value:
        for j in tuple_vowels:
            if i == j:
                print(i)

str_value = input("Enter the value : ")
count(str_value)