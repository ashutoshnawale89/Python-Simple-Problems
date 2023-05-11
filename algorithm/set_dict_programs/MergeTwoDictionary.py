# Dictionary program: Merge two dictionaries


def mergeTwoDictionary():
    student_id1 = {111: "Eric", 112: "Kyle", 113: "Butters"}
    student_id2 = {114: "Ram", 115: "priti", 116: "Yogesh"}
    print("original dictionary 1 is : ", student_id1)
    print("original dictionary 2 is : ", student_id2)
    for i in student_id2:
        student_id1[i] =student_id2[i]
    print("After merge : ", student_id1)
mergeTwoDictionary()