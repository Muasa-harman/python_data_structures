import json

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

user = User('Harman',31)

def encode_user(o):
    if isinstance(o,User):
        return {'name':o.name, 'age':o.age , o.__class__.__name__: True}
    else :
        raise TypeError('Object of type user is not JSON serialisable')

userJSON = json.dumps(user,default=encode_user)
print(userJSON)