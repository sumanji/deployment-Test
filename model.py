from pydantic import BaseModel
from typing import Optional
class message_(BaseModel):
    question:str
    answer: Optional[str] = None