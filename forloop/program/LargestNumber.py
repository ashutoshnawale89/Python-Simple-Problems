#   Write a program that takes a list of numbers as
#   input and outputs the largest number in the list.

loop_length= range(int(input("Enter loop length")))
arr = [0]
sum=0
for loop in loop_length:
    value = int(input("Enter value"))
    arr.insert(loop , value)

for loop in arr :
    if(sum < loop):
        sum = loop
else:
    print("Largest Value is ",sum)