print("Welcome to the program")

# def parentFunction(x):
#     def childFunction(y):
#         return x + y
#     return childFunction
#
#
# obj1 = parentFunction(5)
# print(obj1)
# obj2 = obj1(6)
# print(obj2)
#
# def parent(x):
#     return x*x
# def child(func,x):
#     return func(x)
# result = child(parent , 5)
# print(result)
#
# def parentFunc(name):
#     def child():
#         return "Hello",name
#     return child
#
# obj1 = parentFunc("Harshal")
# print(obj1())

# def parentClass(func):
#     def childClass():
#         print("Child class")
#         func()
#     return childClass
# def ordinary():
#     print( "Hello got Ordinary method")
#
# obj1 = parentClass(ordinary)
# obj1()
#
# def parentClass(func):
#     def childClass(d,z):
#         print(d,z)
#         if d==0 or z==0:
#             print("Whops cannot be divide '0' ")
#             return
#         return func(d,z)
#     return childClass
# @parentClass
# def ordinaryFun(x,y):
#     return x/y
# print(ordinaryFun(5,5))
#
# def method1(func):
#     def subMethod1(*args, **kwargs):
#         print("Sub-Method 1")
#         func(*args , **kwargs)
#         print("Sub Method  1")
#     return subMethod1
#
# def method2(func):
#     def subMethod2(*args, **kwargs):
#         print("Sub-Method 2")
#         func(*args , **kwargs)
#         print("Sub Method  2")
#     return subMethod2
#
# @method1
# @method2
# def ordinary(name):
#     print("Welcome",name)
#
# ordinary("Jayprakash")
#
# list_name = [12,15,"jh",85,"kj"]
# iterator = iter(list_name)
# print(next(iterator))
# infinte =count(1,2)
# for i in range(5):
#     print(next(infinte))









