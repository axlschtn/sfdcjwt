import os
from fastapi import FastAPI, Depends, HTTPException
from simple_salesforce import Salesforce

app = FastAPI()

# os.environ.get()
# os.getenv('KEY')
def sf_connect():
    try:
        return 'ok'
    except:
        raise HTTPException(
            status_code=404,
            detail=str('OUPSSS')
        )
    

@app.get('/')
async def get_index(sf_connect = Depends(sf_connect)) -> str:
    return sf_connect