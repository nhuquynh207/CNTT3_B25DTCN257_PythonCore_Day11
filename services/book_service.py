from sqlalchemy.orm import Session
from sqlalchemy import or_
from models.book_model import Book
from schemas.book_schema import BookCreate, BookUpdate


def create_book(db: Session, book: BookCreate):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def get_books(db: Session):
    return db.query(Book).all()


def get_book_by_id(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def update_book(db: Session, book_id: int, book_in: BookUpdate):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None

    update_data = book_in.model_dump(exclude_unset=True)

    for field in update_data:
        setattr(book, field, update_data[field])

    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None

    db.delete(book)
    db.commit()
    return book


def search_books(db: Session, query: str):
    return db.query(Book).filter(
        or_(
            Book.title.ilike(f"%{query}%"),
            Book.author.ilike(f"%{query}%"),
            Book.category.ilike(f"%{query}%")
        )
    ).all()


def borrow_warning(db: Session, threshold: int = 5):
    return db.query(Book).filter(
        Book.available_quantity <= threshold
    ).all()


def top_borrowed(db: Session, limit: int = 5):
    return db.query(Book).order_by(
        Book.borrow_count.desc()
    ).limit(limit).all()