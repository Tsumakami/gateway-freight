from typing import List
from models.request import Request
from models.response import Response
from models.services import Services


class CotationService:
    
    @staticmethod
    def quote(request: Request) -> List[Response]:
        response: List[Response] = list()

        for service in Services:
            resp = Response()
            resp.courier = service.name
            response.append(resp)

        return response