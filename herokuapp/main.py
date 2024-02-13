from fastapi import FastAPI, status
from fastapi.security import OAuth2PasswordBearer
from herokuapp.routes import (
    authentication,
    salesforce,
    user
)

app = FastAPI(
    title='Rayside Corpotation ®',
    version='0.0.1',
    summary='The Summary here',
    description='Rayside Corpotation',
)

app.include_router(salesforce.router)
app.include_router(authentication.router)
app.include_router(user.router)

@app.get(
    '/',
    tags=['Home']
)
async def get_index():
    return {
        'status_code': status.HTTP_200_OK,
        'message': 'Welcome to Rayside, the lead you are'        
    }