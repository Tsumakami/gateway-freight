import json

from models.response import Response

class MapResponse:
    
    @staticmethod
    def fromCorreiosResp(resp):
        response = Response()
        response.cost = float(resp['Valor'].replace(',','.'))
        response.delivery_time = int(resp['PrazoEntrega'])
        response.courier = 'Correios'

        if resp['Erro'] != '0':
            response.message = resp['Erro']
            
        return response

    @staticmethod
    def fromJadlogResp(resp):
        response = Response()
        
        response.cost = resp['cost']
        response.delivery_time = resp['delivery_time']
        response.courier = resp['courier']

        if resp['message'] != None:
            response.message = resp['message']
            
        return response