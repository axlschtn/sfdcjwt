import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    SF_CONSUMER_KEY: str = os.getenv('SF_CONSUMER_KEY')
    SF_USERNAME: str = os.getenv('SF_USERNAME')
    SF_LOGIN_URL: str = os.getenv('SF_LOGIN_URL')
    SF_PRIVATE_KEY: str = os.getenv('SF_PRIVATE_KEY')
    SF_TOKEN_SERVICE: str = os.getenv('SF_TOKEN_SERVICE')
    SF_GRANT_TYPE: str = os.getenv('SF_GRANT_TYPE')
    SF_TOKEN_REVOKE: str = os.getenv('SF_TOKEN_REVOKE')
    
    

