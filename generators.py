# def mygenerato():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerato()

# value = next(g)
# print(value)

# # for i in g:
# #     print(i)

# def fibonacci(limit):
#     a,b = 0 , 1 
#     while a < limit:
#         yield a
#         a, b = b , a + b
# fib = fibonacci(30)
# for i in fib:
#     print(i)

mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print (i)