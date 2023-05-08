#Write a Python program to find the sum of all prime numbers in a given range.

def sumofEvenNumber(value):
    index = range(value)
    arr_list = []
    arr_index = 0
    for i in index:
        count = i//2
        num = 0
        while count != 0:
            if i % count == 0:
                num = num + 1
            count =count - 1
        if num == 1:
            arr_list.insert(arr_index, i)
            arr_index = arr_index + 1
    print(arr_list)
    print(sum(arr_list))


value = int(input("Enter the Value "))
sumofEvenNumber(value)