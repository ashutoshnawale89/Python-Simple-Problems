# Write a Python program that uses the "assert" statement to raise an exception if a condition is not met.

try:
    value1 = int(input(" Enter value: "))
    assert value1 >= 18
except Exception:
    print("Exception occure : Invalid Age")
else:
    print("Suceesfully Eligible for vote ")
finally:
    print("It is citizen of INDIA")