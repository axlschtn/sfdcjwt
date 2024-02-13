import requests
import jwt
from .settings import Settings
from herokuapp.models.auth import RequestJWTPayload

class SalesforceAuth():
    
    @property
    def generate_token(self):
        return RequestJWTPayload(
            iss=Settings.SF_CONSUMER_KEY,
            sub=Settings.SF_USERNAME,
            aud=Settings.SF_LOGIN_URL
        ).__dict__    
    
    def post_token(self):
        r = requests.post(
            f'{Settings.SF_LOGIN_URL}{Settings.SF_TOKEN_SERVICE}',
            data = {
                'grant_type': Settings.SF_GRANT_TYPE,
                'assertion': jwt.encode(
                    self.generate_token,
                    Settings.SF_PRIVATE_KEY,
                    algorithm="RS256"
                )
            }
        )
        return r

    