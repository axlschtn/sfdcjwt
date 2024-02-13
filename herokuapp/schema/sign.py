from pydantic import BaseModel
from .user import User
'''
@@@@@@@@@@@@@@@@@@@@@@@@@@@
 Authentication / Passport
@@@@@@@@@@@@@@@@@@@@@@@@@@@
'''

class Authentication(User):
    pass

class AuthenticationIn(Authentication):
    pass

class AuthenticationUp(Authentication):
    pass