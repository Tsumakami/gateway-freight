from codecs import iterdecode
import csv

from fastapi import File
from models.contingency import Contingency, ContingencyCreate
from models.response import Response
from config.database import Session

class ContingencyService:
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
    
        