from fastapi import FastAPI

from database import Base, engine
from routers import book_router
from models.author_models import AuthorModel
from models.book_model import BookModel

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(book_router.router)