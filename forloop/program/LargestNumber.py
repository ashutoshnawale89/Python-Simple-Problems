#   Write a program that takes a list of numbers as
#   input and outputs the largest number in the list.

loop_length= range(int(input("Enter loop length")))
arr = [0]
sum_Fibbo=0
for loop in loop_length:
    count = int(input("Enter value"))
    arr.insert(loop, count)

for loop in arr :
    if(sum_Fibbo < loop):
        sum_Fibbo = loop
else:
    print("Largest Value is ", sum_Fibbo)