from typing import List
from models.request import Request
from models.response import Response
from models.services import Services
from services.contingency_service import ContingencyService
from services.cotation import CotationInterface

class CotationService:
    
    @staticmethod
    def quote(request: Request) -> List[Response]:
        response: List[Response] = list()

        for service in Services:

            if service.value != None:
                cotationService: CotationInterface = service.value
                resp = cotationService.quote(request= request)
                
                if resp == None:
                    print(f'{type(cotationService).__name__} returned None on result. ')
                    continue

                if resp.message != None:
                    print(f'Cotation fail in {type(cotationService).__name__}.')
                else:
                    response.append(resp)

        if len(response) == 0:
            resp = ContingencyService.quote(request)
            if resp != None:
                response.append(resp)

        return response