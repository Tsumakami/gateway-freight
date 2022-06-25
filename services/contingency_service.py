from models.request import Request
from models.response import Response
from .cotation import CotationInterface


class CorreiosService(CotationInterface):
    
    def quote(self, request: Request) -> Response:
        print('Cotating in Contigency...')
