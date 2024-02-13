from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from herokuapp.infrastructure.salesforce import SalesforceAuth
from herokuapp.models.auth import TokenResponse, TokenError

router = APIRouter()

@router.get(
    '/token',
    response_model=TokenResponse
)
async def get_token(
    auth: Annotated[
        None,
        Depends(SalesforceAuth().post_token)
    ]
) -> TokenResponse | TokenError:
    if auth.status_code == 200:
        return TokenResponse(**auth.json())
    else:
        return TokenError(**auth.json())