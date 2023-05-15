class InvalidAgeException(Exception):
    pass

number = 18

age = int(input("Enter the age : "))
try:
 if age >= number:
    print("Eligible")
 else:
     raise InvalidAgeException

except InvalidAgeException:
 print("Exception occurred: Invalid Age")
