# Make a decorator that prints the function name before and after it is called.

def printFunction1(func):
    def subPrintFunction1(*args, **kwargs):
        print("Sub function-1 before Excution Done...")
        func(*args, **kwargs)
        print("Sub function-1 after Excution Done...")
    return subPrintFunction1


def printFunction2(func):
    def subPrintFunction2(*args, **kwargs):
        print("Sub function-2 before Excution Done...")
        func(*args, **kwargs)
        print("Sub function-2 after Excution Done...")
    return subPrintFunction2

@printFunction1
@printFunction2
def ordinaryFunction(name):
    print("Welcome ", name, "......!")


name = "Nikita"
ordinaryFunction(name)
