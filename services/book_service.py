from sqlalchemy.orm import Session
from fastapi import HTTPException
from models.book_model import BookModel,Base
from schemas.book_schema import BookCreateSchema,BookResponseSchema,BookUpdateSchema,BaseModel

def update_book(db: Session, book_id: int, book_in: BookUpdateSchema):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        return None
    for key, value in book_in.model_dump(exclude_unset=True).items():
        setattr(book, key, value)
    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        return False
    db.delete(book)
    db.commit()
    return True

def create_book(db:Session,new_book: BookCreateSchema):
    db_book = BookModel.model_dump(**new_book.model_dump())

    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_all_books(db:Session):
    return db.query(BookModel).all()

def get_book_by_id(db:Session,book_id: int):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404,detail="Không tìm thấy sách")
    return book


