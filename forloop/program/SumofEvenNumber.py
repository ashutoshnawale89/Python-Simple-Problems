
#Write a program that takes a list of integers as input
# and outputs the sum of all the even numbers in the list.


loop_length= range(int(input("Enter loop length")))
arr = [0]
sum=0
for loop in loop_length:
    value = int(input("Enter value"))
    arr.insert(loop , value)

for loop in arr :
    if(loop % 2 == 0):
        sum += loop
else:
    print("Sum of all even is ",sum)



