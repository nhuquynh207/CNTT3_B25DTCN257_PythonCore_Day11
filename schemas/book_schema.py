from pydantic import BaseModel,ConfigDict
from typing import Optional

class BookCreateSchema(BaseModel):
    code: str
    title: str
    price: float
    pages: int
class BookResponseSchema(BookCreateSchema):
    id: int
    model_config = ConfigDict(from_attributes=True)

class BookUpdateSchema(BaseModel):
    title: Optional[str]= None
    author: Optional[str]=None
    price: Optional[float]=None
    quantity: Optional[int]=None