from typing import Annotated, Union
from fastapi import APIRouter, Depends, status, HTTPException
from herokuapp.infrastructure.salesforce import SalesforceAuth
from herokuapp.schema.token import TokenResponse, TokenError
from herokuapp.common.utils import store_token_data

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
    if auth.status_code == status.HTTP_400_BAD_REQUEST:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail= {'status_code': status.HTTP_400_BAD_REQUEST}
        )
    return 'ok'