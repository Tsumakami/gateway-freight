from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from services.authentication import Authentication
from services.cotation_service import CotationService

from models.request import Request
from models.response import Response

app = FastAPI()
security = HTTPBasic()

@app.post('/quote')
async def quote(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    Authentication.authenticate(credentials= credentials)
    
    response = CotationService.quote(request)

    return response

