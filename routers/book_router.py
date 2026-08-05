from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas.book_schema import BookCreateSchema, BookUpdateSchema, BookResponseSchema
from services import book_service

router = APIRouter(
    prefix="/api/v1/books",
    tags=["Book Controller"]
)


@router.get("/", response_model=list[BookResponseSchema])
def get_all_books(db: Session = Depends(get_db)):
    return book_service.get_all_books(db)


@router.get("/{book_id}", response_model=BookResponseSchema)
def get_book_by_id(book_id: int, db: Session = Depends(get_db)):
    book = book_service.get_book_by_id(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


@router.post("/", response_model=BookResponseSchema)
def create_book(book: BookCreateSchema, db: Session = Depends(get_db)):
    return book_service.create_book(db, book)


@router.put("/{book_id}", response_model=BookResponseSchema)
def update_book(book_id: int, book: BookUpdateSchema, db: Session = Depends(get_db)):
    update_book = book_service.update_book(db, book_id, book)

    if not update_book:
        raise HTTPException(status_code=404, detail="Book not found")

    return update_book


@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = book_service.delete_book(db, book_id)

    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Delete successfully"}