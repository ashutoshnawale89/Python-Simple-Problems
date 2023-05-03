print("Hello.........")

# ..............................................Day 1 Topics....................................................
number1 =25
print("number1  ",number1)

number2=35
number1=number2
print("number1  ", number1)

color1="Red"
print("color1 ", color1)
color2="Blue"
color1=color2
print("color1 ", color1)

print("Name", 25 , "DOB")
print( number2 , color1)

print(number2+number1)

#..............................................Day 2 Topics......................................................

#Python List Data Type
arr=["Banana" , "Apple" , "Grapes" , "Mango"]
print(arr)

# Python Numeric Data type
num1 = 5
print(num1, 'is of type', type(num1))

num2 = 2.0
print(num2, 'is of type', type(num2))

num3 = 1+2j
print(num3, 'is of type', type(num3))

#Python Tuple Data Type
tuple=("Banana" , "Apple" , "Grapes" , "Mango")
print(tuple)

#String
name = 'Python'
print(name)

message = 'Python for beginners'
print(message)

# Python Dictionary Data Type. (KEY and VALUE pair)
capital_city = {'Nepal': 'Kathmandu', 'Italy': 'Rome', 'England': 'London'}

print(capital_city)
print(capital_city['Nepal'])  # prints Kathmandu

#Python Type Conversion ---- Implicit Conversion - automatic type conversion
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))


#Python Type Conversion ---- Explicit Conversion - manual type conversion
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))


# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)  

print('Data type of num:', type(num))
