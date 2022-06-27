from enum import Enum

from services.correios_service import CorreiosService
from services.jadlog_service import JadlogService

class Services(Enum):
    CORREIOS = CorreiosService()
    JADLOG = JadlogService()
    CONTINGENCY = None
