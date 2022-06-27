from typing import Union
from pydantic import BaseModel

class Response(BaseModel):
    courier: str = None
    message: Union[str, None] = None
    cost: float = None
    delivery_time: int = None
