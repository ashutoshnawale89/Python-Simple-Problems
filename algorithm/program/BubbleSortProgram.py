#Write a Python program to sort a list of numbers using the bubble sort algorithm.

def sorting(value):
    size = len(value)
    count_i = 0
    for i in value:
        count_j = 0
        for j in value:
            if i < j:
                temp = value[count_i]
                value[count_i] = value[count_j]
                value[count_j] = temp
            count_j = count_j + 1
        count_i = count_i + 1
    print(value)


value = [12,78,1,45,8,3,45,15]
sorting(value)