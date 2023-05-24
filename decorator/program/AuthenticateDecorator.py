# Create a decorator @authenticated that checks if a user is authenticated before executing a function.
list_user = ["ashish","akshay","shadab","yogesh",'aslam']

def authenticate(func):
    def subAuthenticate(value):
        for i in list_user:
            if value == i:
                print("User is valid....")
                return func(value)
        print("User not Authenticate...!")
        return

    return subAuthenticate

@authenticate
def ordinaryFunction(value):
    print("User check authenicate data is Succesfully done......")

ordinaryFunction("aslam")
