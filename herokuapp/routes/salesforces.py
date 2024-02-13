from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from herokuapp.infrastructure.salesforce import SalesforceAuth
from herokuapp.models.auth import TokenResponse

router = APIRouter()

@router.get(
    '/token',
    response_model=TokenResponse
)
async def get_token(
    auth: Annotated[
        None,
        Depends(SalesforceAuth)
    ]
) -> TokenResponse:
    return TokenResponse(**auth.post_token().json())
    