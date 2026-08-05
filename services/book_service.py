from sqlalchemy.orm import Session
from models.book_model import BookModel
from schemas.book_schema import BookCreateSchema, BookUpdateSchema


def get_all_books(db: Session):
    return db.query(BookModel).all()
def get_book_by_id(db: Session, book_id: int):
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def create_book(db: Session, book: BookCreateSchema):
    new_book = BookModel(
        title=book.title,
        author=book.author,
        price=book.price,
        quantity=book.quantity
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


def update_book(db: Session, book_id: int, book: BookUpdateSchema):
    old_book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not old_book:
        return None

    update_data = book.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(old_book, key, value)

    db.commit()
    db.refresh(old_book)
    return old_book
def delete_book(db: Session, book_id: int):
    book = db.query(BookModel).filter(BookModel.id == book_id).first()

    if not book:
        return None
    db.delete(book)
    db.commit()
    return book