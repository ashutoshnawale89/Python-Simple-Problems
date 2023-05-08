#Write a Python program to find the second largest number in a list.
def secondLargest_Number(number_list):
    firstLargest_Number = 0
    secondLargest_Number = 0
    for i in number_list:
        if i > firstLargest_Number:
            firstLargest_Number = i

    for i in number_list:
        if secondLargest_Number < i:
            if firstLargest_Number != i:
                secondLargest_Number = i

    print(secondLargest_Number)

number_list = [12 , 14, 8 , 78 , 45,47,49,78]
secondLargest_Number(number_list)