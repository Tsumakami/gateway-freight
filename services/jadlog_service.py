import json
import requests
from requests.auth import HTTPBasicAuth
from models.request import Request
from models.response import Response
from utils.map_response import MapResponse
from .cotation import CotationInterface

class JadlogService(CotationInterface):
    endpoint:str = 'http://172.31.40.105:8083/quote'
    user: str = 'admin'
    password: str = 'admin123'

    def quote(self, request: Request) -> Response:
        print(f'Cotating {request} in JadLog...')

        try:
            auth = HTTPBasicAuth(username= self.user, password= self.password)
            data = json.dumps(request.__dict__)

            response = requests.post(url= self.endpoint, data= data, auth= auth, timeout=20)
            print(response.status_code)

            if response.status_code == 200:
                print(response.text)
                
                return MapResponse.fromJadlogResp(json.loads(response.text))
        except Exception as error:
            print(f'fail at cotation request {request} on endpoint: {self.endpoint}. Error: {error}')

        return None