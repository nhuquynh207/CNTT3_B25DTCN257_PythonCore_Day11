from pydantic import BaseModel, ConfigDict


class BookBase(BaseModel):
    title: str
    author: str
    category: str
    price: float
    borrow_count: int = 0
    available_quantity: int = 0


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    category: str | None = None
    price: float | None = None
    borrow_count: int | None = None
    available_quantity: int | None = None


class BookResponse(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)