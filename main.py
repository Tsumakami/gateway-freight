from fastapi import Depends, FastAPI, File, UploadFile, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Response as HTTPResponse

from services.authentication import Authentication
from services.contingency_service import ContingencyService
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

@app.post("/contingecy/uploadfile")
async def create_upload_file(file: UploadFile = File(...), credentials: HTTPBasicCredentials = Depends(security)):
    Authentication.authenticate(credentials= credentials)
    
    ContingencyService.save_contingency(file)

    return HTTPResponse(status_code=status.HTTP_201_CREATED)
    
