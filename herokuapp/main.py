from fastapi import FastAPI
from herokuapp.routes import salesforces

app = FastAPI()

app.include_router(salesforces.router)

@app.get('/')
async def get_index():
    return 'ok'