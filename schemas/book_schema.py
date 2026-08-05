from pydantic import BaseModel, ConfigDict


class BookCreateSchema(BaseModel):
    title: str
    author: str
    price: float
    quantity: int


class BookUpdateSchema(BaseModel):
    title: str | None = None
    author: str | None = None
    price: float | None = None
    quantity: int | None = None
class BookResponseSchema(BaseModel):
    id: int
    title: str
    author: str
    price: float
    quantity: int

    model_config = ConfigDict(from_attributes=True)