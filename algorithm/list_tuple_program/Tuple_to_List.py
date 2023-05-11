# Tuple program: Convert a tuple to a list and add a new element

def covert():
    tuple_value = (45, 55, 65, 85, 52, 12)
    list_value = []
    print("Tuple ", tuple_value)
    print("original list ", list_value)
    for i in tuple_value:
        list_value.append(i)
    print("Convert to list ", list_value)

covert()