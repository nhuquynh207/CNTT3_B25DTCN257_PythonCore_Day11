from pydantic import BaseModel, ConfigDict


class AuthorResponseSchema(BaseModel):
    id: int
    name: str
    email: str

    model_config = ConfigDict(from_attributes=True)


class BookCreateSchema(BaseModel):
    title: str
    price: float
    author_id: int


class BookResponseSchema(BaseModel):
    id: int
    title: str
    price: float
    author_id: int
    author: AuthorResponseSchema

    model_config = ConfigDict(from_attributes=True)