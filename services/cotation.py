from models.response import Response
from models.request import Request


class CotationInterface:

    def quote(self, request: Request) -> Response:
        pass