try:
    numerator = 10
    denominator = 0

    result = numerator/denominator

    print(result)
except:
    print("Error: Denominator cannot be 0.")

def method1():
    print(" Method --  1")
    try:

        even_numbers = [2, 4, 6, 8]
        print(even_numbers[5])
        print(even_numbers[2]/0)

    except ZeroDivisionError:
        print("Denominator cannot be 0.")

    except IndexError:
        print("Index Out of Bound.")

method1()

def method2():
    # program to print the reciprocal of even numbers
    print(" Method --  2")
    try:
        num = int(input("Enter a number: "))
        assert num % 2 == 0
    except:
        print("Not an even number!")
    else:
        reciprocal = 1 / num
        print(reciprocal)
method2()

def method3():
    print(" Method --  3")
    try:
        numerator = 10
        denominator = 2

        result = numerator / denominator

        print(result)
    except:
        print("Error: Denominator cannot be 0.")

    finally:
        print("This is finally block.")
method3()