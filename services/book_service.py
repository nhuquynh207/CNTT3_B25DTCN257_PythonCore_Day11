from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.book_model import BookModel
from models.author_models import AuthorModel
from schemas.book_schema import BookCreateSchema


def get_books(db: Session):
    return db.query(BookModel).all()


def get_book(db: Session, book_id: int):
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def create_book(db: Session, book_in: BookCreateSchema):
    author = db.query(AuthorModel).filter(
        AuthorModel.id == book_in.author_id
    ).first()

    if not author:
        raise HTTPException(
            status_code=400,
            detail=f"Mã tác giả author_id = {book_in.author_id} không tồn tại trong hệ thống CSDL!"
        )

    new_book = BookModel(
        title=book_in.title,
        price=book_in.price,
        author_id=book_in.author_id
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book