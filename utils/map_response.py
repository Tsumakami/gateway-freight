import json

from models.response import Response

class MapResponse:
    
    @staticmethod
    def fromCorreiosResp(resp):
        response = Response()
        response.cost = resp['Valor']
        response.delivery_time = resp['PrazoEntrega']
        response.courier = 'Correios'

        if resp['Erro'] != '0':
            response.message = resp['Erro']
            
        return response