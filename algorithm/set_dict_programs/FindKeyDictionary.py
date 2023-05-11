# Dictionary program: Find the key with the maximum value in a dictionary

def findKeyMaximumValue():
    student_id1 = {111: "Eric", 112: "Kyle", 113: "Butters", 114: "Ram", 115: "priti", 116: "Yogesh"}
    print("original dictionary 1 is : ", student_id1)
    value = ""
    for i in student_id1:
        if student_id1[i] > value:
            value = student_id1[i]

    for i in student_id1:
        if value == student_id1[i]:
            print("The Index is : ", i, " and the value is ", value)
findKeyMaximumValue()