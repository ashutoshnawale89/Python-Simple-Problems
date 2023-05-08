
#Write a program that takes a list of integers as input
# and outputs the sum of all the even numbers in the list.


loop_length= range(int(input("Enter loop length")))
arr = [0]
sum_Fibbo=0
for loop in loop_length:
    count = int(input("Enter value"))
    arr.insert(loop, count)

for loop in arr :
    if(loop % 2 == 0):
        sum_Fibbo += loop
else:
    print("Sum of all even is ", sum_Fibbo)



