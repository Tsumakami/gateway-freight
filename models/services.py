from enum import Enum

from services.correios_service import CorreiosService

class Services(Enum):
    CORREIOS = CorreiosService()
    CONTINGENCY = ""
