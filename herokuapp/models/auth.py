from pydantic import BaseModel
import time

'''
@@@@@@@@@@@@@@@@@@@@@@@@@@@
    Response Type Token
@@@@@@@@@@@@@@@@@@@@@@@@@@@
{
    'access_token': '00D5J000001QKnh!ARwAQEVRRJl0YdJnST9oK8Ragl2nIP5lEw8lb619sw_7ZT2CLA5hFcWrnlXe3xJfF8GVUEmNRzhrc4LziA4PZWZUaDAVK_rb',
    'scope': 'openid api id forgot_password full',
    'instance_url': 'https://d5j000001qknhuag-dev-ed.my.salesforce.com',
    'id': 'https://login.salesforce.com/id/00D5J000001QKnhUAG/0055J000000aE3cQAE',
    'token_type': 'Bearer'
}
'''

class TokenResponse(BaseModel):
    access_token: str
    scope: str
    instance_url: str
    id: str
    token_type: str

class TokenError(BaseModel):
    error: str
    error_description: str
    
class ResponseTokenService(BaseModel):
    data: TokenResponse


class RequestJWTPayload(BaseModel):
    iss: str
    sub: str
    exp: int = int(time.time()) - 1
    aud: str