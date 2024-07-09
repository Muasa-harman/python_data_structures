# # synta error
# my_dict = {'name', 'Harman'}
# a = 5 + '10'
# print(a)

# try:
#     a = 5 / 0
# except Exception as e:
#     print(e)    

# try:
#     a = 5 / 1
#     b = a + 4
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e) 

# else:
#     print('Everything is fine')
# finally:
#     print('cleaning up...')    
#            

class ValueTooHighError(Exception):
    pass

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(y):
    if y > 100:
        raise ValueTooHighError('Value too high')
    if  y < 5:
        raise ValueTooSmallError('Value is too small', y)
    
try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message,e.value)            