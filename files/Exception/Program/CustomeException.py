class CustomeException(Exception):
    pass


try:
    value1 = int(input(" Enter value: "))
    if value1 >= 18:
        print("Suceesfully Eligible for vote ")
    else:
        raise CustomeException

except CustomeException:
    print("Exception occure : Invalid Age")