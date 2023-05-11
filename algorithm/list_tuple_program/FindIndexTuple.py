#Tuple program: Find the index of an element in a tuple

def findIndex(tuple_value):
    for i in tuple_value:
        print("The value is ", i, "index is ", tuple_value.index(i))

tuple_value = ("Hello", "Hii", "Where", "Why")
findIndex(tuple_value)