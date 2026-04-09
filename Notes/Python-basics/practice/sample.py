# # # a = "abc"
# # # b = 10
# # # print(isinstance(a, int))

# # # # ─── MULTIPLE ASSIGNMENT ───
# # # a = b = c = 0 # teeno ek saath 0
# # # x, y, z = 1, 2, 3 # unpacking — Java mein alag alag likhna padta

# # # # ─── SWAP — Python ka magic ───
# # # a, b = 10, 20
# # # a, b = b, a # swap — koi temp variable nahi chahiye!
# # # # Java mein: int temp = a; a = b; b = temp;


# # # list1 = ["ABC", "CDE", "DEF"]

# # # for idx, val in enumerate(list1):
# # #     print(f"idex is {idx} and value is {val}")


# # # if list1[1] == "CDE" :
# # #     print("OKAY")
# # # else :
# # #     print("No")


# # # def greet(name : str) -> str:
# # #     return(f"hey very good morning {name}")

# # # print(greet("BRUNI"))


# # # z = lambda a,v,x : ( a*x +v)

# # # print(z(1,2,3))

# # # sq = []
# # # for i in range(1, 11):
# # #     sq.append(i*i)


# # # print(sq)

# # # sqs = [ i * i for i in range(1,11)]

# # # print(sqs)

# # # config = {"hey" : "HIII", "Heelo" : "wqonxd"}

# # # new_config = { k.upper() : v for k,v in config.items()}
# # # print(config.items())
# # # print(new_config)

# # # decorators


# # # # Step 1: Normal function
# # # def say_hello():
# # #     print("HEY HI HELLO")

# # # # Step 2: Decorator function
# # # def my_decorator(func):
# # #     def wrapper():
# # #         print("Before FUnc")
# # #         func()
# # #         print("After Func")
# # #     return wrapper

# # # # Step 3: Apply decorator

# # # @my_decorator
# # # def say_hello():
# # #     print("Hello Bhai")

# # # say_hello()

# # import time
# # # ORG FUN STe 1
# # def org_fun():
# #     print("Workstarted")
# #     time.sleep(2)
# #     print("WorkEnded")

# # # CReate wrapper step 2

# # def wrapper_fun(func):
# #     def wrapper():
# #         start = time.time()
# #         func()
# #         end = time.time()
# #         print("Time take",  end-start)
# #     return wrapper


# # # new_fun = wrapper_fun(org_fun)

# # @wrapper_fun
# # def newFun():
# #     pass

# # newFun()


# # # import time

# # # def wrapper_fun(func):
# # #     def wrapper():
# # #         start = time.time()
# # #         func()
# # #         end = time.time()
# # #         print("Time take", end - start)
# # #     return wrapper

# # # @wrapper_fun
# # # def org_fun():
# # #     print("Workstarted")
# # #     time.sleep(2)
# # #     print("WorkEnded")

# # # org_fun()





# def my_decor(func):
#     def wrapper():
#         print("YE NAYA DALA HAI")
#         func()
#         print("NAYA hai YE BHI")
#     return wrapper

# @my_decor
# def apna_func():
#     print("YE PURANA MAAL HAI")


# # apna_func()
# from functools import wraps

# def multiArgDecor(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Make ladle meoww")
#         res = func(*args, **kwargs)
#         print(res)
#         print("Gop Gop Gop")
#     return wrapper

# @multiArgDecor
# def function(list : list):
#     """This function adds two numbers"""
#     ans = 1
#     for i in list:
#         ans *= i
#     return ans

# function([1,2,3,4,5])

# print(function.__name__)
# print(function.__doc__)


# def repeat(n):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             print("SBle phle ye")
#             for i in range(n):
#                 print(f"Execuitng {i+1}")
#                 func(*args, **kwargs)
#             print("Baad mai ye")
#         return wrapper
#     return decorator


# @repeat(5)
# def org(list):
#     print(list)

# # org([12,123,1234])



# import time
# import asyncio
# async def inner(str, coun):
#     await asyncio.sleep(2)
#     print(f"Andar ka {str} {coun}")

# async def fun_async(string : str, count : int):
#     print(f"Called fun {count}")
#     res = await inner(string, count)
#     print(f"Fun ended {count}")


# # async def main():
#     # await asyncio.gather(
#     #     fun_async("One", 1),
#     #     fun_async("Two", 2),
#     #     fun_async("Three", 3)
#     # )
    

# # asyncio.run(main())

# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def sound(self):
#         print(f"Name is {self.name} , sound different from human")

# a = Animal("Jaanwar")
# a.sound()


# class Kutta(Animal):
#     def __init__(self, names, breed):
#         super().__init__(names)
#         self.names = names
#         print(f"Kutta hai ye jiska naam {names} hai aur nasal {breed} h")
    
#     def sound(self):
#         print(f"Name is {self.names} , sound different is bhowww")


# d = Kutta("kukur", "desi")
# d.sound()

from typing import TypedDict
from pydantic import BaseModel

# Blueprint banao
class User(BaseModel):
    name: str
    age: int
    email: str

# Ab yeh dictionary User ka structure follow karegi
user = User(
    name="Ramu",
    age='25'
    # email missing
)
print(user)