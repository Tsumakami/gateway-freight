from codecs import iterdecode
import csv

from fastapi import File
from models.contingency import Contingency, ContingencyBase, ContingencyCreate, ContingencySchema
from models.request import Request
from models.response import Response
from config.database import Session
from services.cotation import CotationInterface

class ContingencyService(CotationInterface):
    @staticmethod
    def save_contingency(file: File) -> Response:
        print(f'Cotating {file.filename} in Contigency...')

        content = file.file
        reader = csv.reader(iterdecode(content, "utf-8"), delimiter=';')
        
        contingencies = list()

        index = 0
        for row in reader:
            if row == None:
                continue

            if index != 0:
                contingency = ContingencyCreate(
                    zip_code_start = int(row[0]),
                    zip_code_end = int(row[1]),
                    weight_start = float(row[2]),
                    weight_end = float(row[3]),
                    absolute_cost = float(row[4]),
                    delivery_time = int(row[5])
                )
                
                contingency_db = Contingency(**contingency.dict())
                contingencies.append(contingency_db)
            index += 1
            print(row)
            
            with Session as session:
                session.add_all(contingencies)
                session.commit()
    
    def quote(request: Request) -> Response:
        print(f'Cotating {request} in Contingency...')

        with Session as session:
            start_cep = int(request.origin_postal_code.replace('-', ''))
            end_cep = int(request.destination_postal_code.replace('-', ''))
            weight = float(request.package_weight)
            
            queryResult = session.query(Contingency).filter(Contingency.zip_code_start <= start_cep).filter(Contingency.zip_code_end >= end_cep).filter(Contingency.weight_start <= weight).filter(Contingency.weight_end >= weight).first()

            if(queryResult == None):
                return None

            print(queryResult)
            response: Response = Response(
                courier='Contingency',
                delivery_time= queryResult.delivery_time,
                cost=queryResult.absolute_cost)
            
            return response
