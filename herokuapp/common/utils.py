import requests
import jwt
from herokuapp.infrastructure.settings import Settings
from herokuapp.schema.token import RequestJWTPayload

class Request:
    def post(
        service: str,
        data: dict,
        headers: dict = None
    ):
        if service == 'SF_TOKEN_SERVICE':
            data.update({'grant_type': Settings.SF_GRANT_TYPE})
        return requests.post(
            f'{Settings.SF_LOGIN_URL}{getattr(Settings,service)}',
            headers=headers,
            data=data
        )

class JWTtoken:
    
    def generate_token():
        return RequestJWTPayload(
            iss=Settings.SF_CONSUMER_KEY,
            sub=Settings.SF_USERNAME,
            aud=Settings.SF_LOGIN_URL
        ).__dict__
       
    def get_encode():
        return jwt.encode(
            JWTtoken.generate_token(),
            Settings.SF_PRIVATE_KEY,
            algorithm="RS256"
        )

def store_token_data(token):
    with open('herokuapp/data/token_data.txt', 'w') as file:
        file.write(token)
        file.close()

def get_token_data():
    with open('herokuapp/data/token_data.txt', 'r') as file:
        yield file.readline()
        file.close()