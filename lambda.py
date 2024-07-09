# add10 = lambda a: a + 10
# print(add10(5))

# def add10_func(b):
#     return b + 10
# # print(int(add10_func))

# mult = lambda a,b: a*b
# print(mult(2,7))
from functools import reduce
y = [1,2,3,4]

product_a = reduce(lambda a,b:a*b,y)
print(product_a)