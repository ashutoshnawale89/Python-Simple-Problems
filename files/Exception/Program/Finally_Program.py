# Write a Python program that uses the "finally" block to close a file regardless of whether an exception occurs.


try:
    value1 = int(input(" Enter value: "))
    if value1 >= 18:
        print("Suceesfully Eligible for vote ")
    else:
        raise Exception

except Exception:
    print("Exception occure : Invalid Age")
finally:
    print("It is citizen of INDIA")