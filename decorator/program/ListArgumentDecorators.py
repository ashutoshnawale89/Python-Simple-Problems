# Make a decorator that takes a list of functions as its argument and calls all of them before calling the decorated function.

def listDecorator(func):
    def subListDecorator(value_list):
        for i in value_list:
            print(i)
        return func(value_list)
    return subListDecorator
@listDecorator
def ordinaryFinctionList(value_list):
    print("Inside Actutal Function")

ordinaryFinctionList([25,28,78,41,79,65])