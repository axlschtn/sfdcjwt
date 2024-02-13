from typing import List
from fastapi import APIRouter, Body
from herokuapp.schema.user import User, UserUpdate

router = APIRouter(
    tags=['User']
)

'''
    Get All Users
'''
@router.get(
    '/users',
    name='Get all Users'
)
async def get_all_users() -> List[User]:
    return []

'''
    Get User
'''
@router.get(
    '/user/{user_id:str}',
    name='Get Current User Id'
)
async def get_user(
    user_id: str
) -> str:
    return user_id

'''
    Update User
'''
@router.post(
    '/user/{user_id:str}/update',
    name='Update Current Id'
)
async def update_user(
    user_id: str,
    UserUpdate: UserUpdate = Body(...)
) -> bool:
    return True