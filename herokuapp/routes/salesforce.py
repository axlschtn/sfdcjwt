from typing import Annotated, Union
from fastapi import APIRouter, Depends
from herokuapp.infrastructure.salesforce import SalesforceAuth
from herokuapp.schema.token import TokenResponse, TokenError
from herokuapp.common.utils import store_token_data, get_token_data

router = APIRouter(
    tags=['Salesforce']
)

@router.get(
    '/api/token',
    response_model=Union[TokenResponse,TokenError]
)
async def get_token(
    auth: Annotated[
        None,
        Depends(SalesforceAuth.token_service)
    ]
):
    if auth.status_code == 200:
        store_token_data(auth.json().get('access_token'))
        return TokenResponse(**auth.json())
    else:
        return TokenError(
            **auth.json(),
            status_code=auth.status_code
        )

@router.get(
    '/api/revoke-token'
)
async def get_revoked_token(
    auth: Annotated[
        None,
        Depends(SalesforceAuth.token_revoke)
    ]
):
    token = [token for token in get_token_data()]
    print(token[0])
    return 'ok'