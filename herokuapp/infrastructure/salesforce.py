from herokuapp.common.utils import Request, JWTtoken, get_token_data

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
        current_token = [token for token in get_token_data()]
        r = Request.post(
            'SF_TOKEN_REVOKE',
            headers={ 'content-type':'application/x-www-form-urlencoded' },
            data={ 'token': current_token[0] }
        )
        return r

    