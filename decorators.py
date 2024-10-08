# # function decorator
# # @mydecorator
# # def dosomething():
# #     pass
import functools

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# @start_end_decorator
# def add5(a):
#     return a + 5

# result = add5(10)
# print(result)
# # def print_name():
# #     print("Harman")

# # print_name = start_end_decorator(print_name)

# # print_name()    
# # print(help(add5))
# print(add5.__name__)

# # decorators with args
# def repeat(num_times):
#     def decorator_repeat(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = func(*args,**kwargs)
#             return result
#         return wrapper
#     return decorator_repeat    

# @repeat(num_times=4)
# def greet(name):
#     print(f'Hello {name}')

# greet("Harman")

# # nested decorators
# # @debug
# @start_end_decorator
# def say_hello(name):
#     greeting = f'Hello {name}'
#     print(greeting)
#     return greeting

# say_hello('Harman')

class CountCalls:
    def __init__(self,func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is ecuted {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello') 

say_hello()
say_hello()           