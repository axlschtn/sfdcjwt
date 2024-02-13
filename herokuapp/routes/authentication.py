from fastapi import APIRouter, Query
from herokuapp.schema.sign import AuthenticationIn

router = APIRouter(
    tags=['Authentication']
)

@router.post(
    '/signup',
    response_model = AuthenticationIn
)
async def sign_up(
    email: str = Query(...),
    password: str = Query(...)
):
    user = AuthenticationIn(email=email,password=password)
    return user


@router.post(
    '/signin',
    response_model = AuthenticationIn
)
async def sign_up(
    email: str = Query(...),
    password: str = Query(...)
):
    user = AuthenticationIn(email=email,password=password)
    return user
    