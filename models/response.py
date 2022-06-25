import imp
from pydantic import BaseModel

class Response(BaseModel):
    courier: str = None
    message: str = None
    cost: float = None
    delivery_time: int = None

