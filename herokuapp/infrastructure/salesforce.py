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
        )
    
    def post_token(self):
        return requests.post(
            f'{Settings.SF_LOGIN_URL}{Settings.SF_TOKEN_SERVICE}',
            data = {
                'grant_type': Settings.SF_GRANT_TYPE,
                'assertion': jwt.encode(
                    self.generate_token.__dict__,
                    Settings.SF_PRIVATE_KEY,
                    algorithm="RS256"
                )
            }
        )