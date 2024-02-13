from herokuapp.common.utils import Request, JWTtoken

class SalesforceAuth:
    
    def token_service():
        r = Request.post(
            'SF_TOKEN_SERVICE',
            data = {
                'assertion': JWTtoken.get_encode()
            }
        )
        return r

    def token_revoke():
        r = Request.post(
            'SF_TOKEN_REVOKE',
            headers={ 'content-type':'application/x-www-form-urlencoded' },
            data={ 'token': 'acccess_token_here' }
        )
        return r

    